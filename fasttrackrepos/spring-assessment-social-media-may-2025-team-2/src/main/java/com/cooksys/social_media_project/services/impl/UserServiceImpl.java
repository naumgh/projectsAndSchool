package com.cooksys.social_media_project.services.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.dtos.UserRequestDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.entities.Credentials;
import com.cooksys.social_media_project.entities.Profile;
import com.cooksys.social_media_project.entities.Tweet;
import com.cooksys.social_media_project.entities.User;
import com.cooksys.social_media_project.exceptions.BadRequestException;
import com.cooksys.social_media_project.exceptions.NotAuthorizedException;
import com.cooksys.social_media_project.exceptions.NotFoundException;
import com.cooksys.social_media_project.mappers.CredentialsMapper;
import com.cooksys.social_media_project.mappers.ProfileMapper;
import com.cooksys.social_media_project.mappers.TweetMapper;
import com.cooksys.social_media_project.mappers.UserMapper;
import com.cooksys.social_media_project.repositories.TweetRepository;
import com.cooksys.social_media_project.repositories.UserRepository;
import com.cooksys.social_media_project.services.UserService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {
	
	private final UserRepository userRepository;
	private final UserMapper userMapper;
	private final CredentialsMapper credentialsMapper;
	private final ProfileMapper profileMapper;
	private final TweetRepository tweetRepository;
	private final TweetMapper tweetMapper;

	// helper method to check if required fields are null or blank when receiving a user request DTO to create a new user
	@Override
	public void checkRequiredFieldsCreate(UserRequestDto userRequestDto) {
		Credentials credentials = credentialsMapper.dtoToEntity(userRequestDto.getCredentials());
		Profile profile = profileMapper.dtoToEntity(userRequestDto.getProfile());
		if (credentials == null ||
        	credentials.getUsername() == null || credentials.getPassword() == null || 
        	credentials.getUsername().isBlank() || credentials.getPassword().isBlank()) {
			throw new BadRequestException("Error: username and password fields are required to create a new user.");
		}
		else if (profile == null || profile.getEmail() == null || profile.getEmail().isBlank()) {
			throw new BadRequestException("Error: email field is required to create a new user.");
		}
	}

	// helper method to check if required fields are null or blank when receiving a user request DTO to update a user
	@Override
	public void checkRequiredFieldsUpdate(UserRequestDto userRequestDto) {
		Credentials credentials = credentialsMapper.dtoToEntity(userRequestDto.getCredentials());
		if (credentials == null ||
        	credentials.getUsername() == null || credentials.getPassword() == null || 
        	credentials.getUsername().isBlank() || credentials.getPassword().isBlank()) {
			throw new BadRequestException("Error: username and password fields are required when updating a user.");
		}
		if (userRequestDto.getProfile() == null) {
        	throw new BadRequestException("Error: profile is required when updating a user.");
    	}
        Profile profile = profileMapper.dtoToEntity(userRequestDto.getProfile());
        if (profile.getEmail() != null && profile.getEmail().isBlank()) {
            throw new BadRequestException("Error: email field is required when updating a user.");
        }
	}

	// helper method to validate user credentials when updating or deleting a user
	@Override
	public User validateCredentials(CredentialsDto credentialsDto) {
		Credentials credentials = credentialsMapper.dtoToEntity(credentialsDto);
		Optional<User> optionalUser = userRepository.findByCredentials_Username(credentials.getUsername());
		if (optionalUser.isEmpty()) {
			throw new NotFoundException("Error: user with username " + credentials.getUsername() + " does not exist.");
		}
		User userToEdit = optionalUser.get();
		if (!userToEdit.getCredentials().getPassword().equals(credentials.getPassword())) {
			throw new NotAuthorizedException("Error: not authorized to edit user, provided password is incorrect.");
		}
		return userToEdit;
	}

	@Override
	public List<UserResponseDto> getAllUsers() {
		return userMapper.entitiesToDtos(userRepository.findAllByDeletedFalse());
	}

	@Override
	public UserResponseDto createUser(UserRequestDto userRequestDto) {
		checkRequiredFieldsCreate(userRequestDto);
		User newUser = userMapper.dtoToEntity(userRequestDto);
		// throw an error if username already exists and is not deleted
		Optional<User> optionalUser = userRepository.findByCredentials_Username(newUser.getCredentials().getUsername());
		if (!optionalUser.isEmpty() && !optionalUser.get().isDeleted()) {
			throw new BadRequestException("Error: the username " + newUser.getCredentials().getUsername() + " is not available.");
		}
		// if the username already exists but is deleted, re-activate deleted user
		else if (!optionalUser.isEmpty() && optionalUser.get().isDeleted()) {
			optionalUser.get().setDeleted(false);
			return userMapper.entityToDto(userRepository.saveAndFlush(optionalUser.get()));
		}
		return userMapper.entityToDto(userRepository.saveAndFlush(newUser));
	}
	
	@Override
	public UserResponseDto getUser(String username) {
		Optional<User> optionalUser = userRepository.findByCredentials_Username(username);
		if (optionalUser.isEmpty() || optionalUser.get().isDeleted()) {
			throw new BadRequestException("Error: user with username " + username + " could not be found.");
		}
		return userMapper.entityToDto(optionalUser.get());
	}

	@Override
	public UserResponseDto updateUser(String username, UserRequestDto userRequestDto) {
		checkRequiredFieldsUpdate(userRequestDto);
		User userToUpdate = validateCredentials(userRequestDto.getCredentials());
		if (userToUpdate.isDeleted()) {
			throw new NotFoundException("Error: user with username " + username + " could not be found.");
		}
		else if (!userToUpdate.getCredentials().getUsername().equals(username)) {
			throw new BadRequestException("Error: username given in request body does not match username given in URL.");
		}
		Profile profileToUpdate = userToUpdate.getProfile();
		Profile newProfile = profileMapper.dtoToEntity(userRequestDto.getProfile());
		if (newProfile.getFirstName() != null) {
			profileToUpdate.setFirstName(newProfile.getFirstName());
		}
		if (newProfile.getLastName() != null) {
			profileToUpdate.setLastName(newProfile.getLastName());
		}
		if (newProfile.getEmail() != null) {
			profileToUpdate.setEmail(newProfile.getEmail());
		}
		if (newProfile.getPhone() != null) {
			profileToUpdate.setPhone(newProfile.getPhone());
		}
		userToUpdate.setProfile(profileToUpdate);
		return userMapper.entityToDto(userRepository.saveAndFlush(userToUpdate));
	}

	@Override
	public UserResponseDto deleteUser(String username, CredentialsDto credentialsDto) {
		User userToDelete = validateCredentials(credentialsDto);
		userToDelete.setDeleted(true);
		return userMapper.entityToDto(userRepository.saveAndFlush(userToDelete));
	}

	@Override
	public void followUser(String username, CredentialsDto credentialsDto) {
		User userToFollowOtherUser = validateCredentials(credentialsDto);
		Optional<User> optionalUser = userRepository.findByCredentials_UsernameAndDeletedFalse(username);
		if (optionalUser.isEmpty()) {
			throw new NotFoundException("Error: user with username " + username + " cannot be found.");
		}
		User userToBeFollowed = optionalUser.get();
		if (userToFollowOtherUser.getFollowing().contains(userToBeFollowed)) {
			throw new BadRequestException("Error: you already follow this user.");
		}
		userToFollowOtherUser.getFollowing().add(userToBeFollowed);
		userToBeFollowed.getFollowers().add(userToFollowOtherUser);
		userRepository.saveAndFlush(userToFollowOtherUser);
		userRepository.saveAndFlush(userToBeFollowed);
	}

	@Override
	public void unfollowUser(String username, CredentialsDto credentialsDto) {
		User userToUnfollowOtherUser = validateCredentials(credentialsDto);
		Optional<User> optionalUser = userRepository.findByCredentials_UsernameAndDeletedFalse(username);
		if (optionalUser.isEmpty()) {
			throw new NotFoundException("Error: user with username " + username + " cannot be found.");
		}
		User userToBeUnfollowed = optionalUser.get();
		if (!userToUnfollowOtherUser.getFollowing().contains(userToBeUnfollowed)) {
			throw new BadRequestException("Error: you do not currently follow this user.");
		}
		userToUnfollowOtherUser.getFollowing().remove(userToBeUnfollowed);
		userToBeUnfollowed.getFollowers().remove(userToUnfollowOtherUser);
		userRepository.saveAndFlush(userToUnfollowOtherUser);
		userRepository.saveAndFlush(userToBeUnfollowed);
	}

	@Override
	public List<UserResponseDto> getFollowers(String username) {
		Optional<User> optionalUser = userRepository.findByCredentials_UsernameAndDeletedFalse(username);
		if (optionalUser.isEmpty()) {
			throw new NotFoundException("Error: user with username " + username + " cannot be found.");
		}
		// get the followers list then filter through to only include active (not deleted) users
		List<User> allFollowers = optionalUser.get().getFollowers();
		List<User> activeFollowers = new ArrayList<>();
		for (User u : allFollowers) {
			if (!u.isDeleted()) {
				activeFollowers.add(u);
			}
		}
		return userMapper.entitiesToDtos(activeFollowers);
	}

	@Override
	public List<UserResponseDto> getFollowing(String username) {
		Optional<User> optionalUser = userRepository.findByCredentials_UsernameAndDeletedFalse(username);
		if (optionalUser.isEmpty()) {
			throw new NotFoundException("Error: user with username " + username + " cannot be found.");
		}
		// get the following list then filter through to only include active (not deleted) users
		List<User> allFollowing = optionalUser.get().getFollowing();
		List<User> activeFollowing = new ArrayList<>();
		for (User u : allFollowing) {
			if (!u.isDeleted()) {
				activeFollowing.add(u);
			}
		}
		return userMapper.entitiesToDtos(activeFollowing);
	}

	@Override
	public List<TweetResponseDto> getUserFeed(String username){
		Optional<User> optionalUser = userRepository.findByCredentials_Username(username);
		if(optionalUser.isEmpty() || optionalUser.get().isDeleted()) {
			throw new BadRequestException("User was not found"); 
		}		
		//should Retrieve all (non-deleted) tweets authored by the user with the given username, 
		//as well as all (non-deleted) tweets authored by users the given user is following. 
		//This includes simple tweets, reposts, and replies
		User user = optionalUser.get();
		List<User> authors = new ArrayList<>();
	    authors.add(user);
	    authors.addAll(user.getFollowing());
		List<Tweet> tweets = tweetRepository.findAllByAuthorInAndDeletedFalseOrderByPostedDesc(authors);
		return tweetMapper.entitiesToResponseDtos(tweets);
	}

	@Override
	public List<TweetResponseDto> getMentionedTweetsByUsername(String username){
		Optional<User> optionalUser = userRepository.findByCredentials_Username(username);
		if(optionalUser.isEmpty() || optionalUser.get().isDeleted()) {
			throw new BadRequestException("User was not found"); 
		}
		List<Tweet> tweets = tweetRepository.findAllMentioningUser(username);
		return tweetMapper.entitiesToResponseDtos(tweets);
	}

	@Override
	public List<TweetResponseDto> getTweetsByUsername(String username){
		Optional<User> optionalUser = userRepository.findByCredentials_Username(username);
		if(optionalUser.isEmpty() || optionalUser.get().isDeleted()) {
			throw new BadRequestException("User was not found"); 
		}
		List<Tweet> tweets = tweetRepository
			.findAllByAuthorCredentialsUsernameAndDeletedFalseOrderByPostedDesc(username);
		return tweetMapper.entitiesToResponseDtos(tweets);
	}

}
