package com.cooksys.social_media_project.services;

import java.util.List;

import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.dtos.UserRequestDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.entities.User;

public interface UserService {

    void checkRequiredFieldsCreate(UserRequestDto userRequestDto);

    void checkRequiredFieldsUpdate(UserRequestDto userRequestDto);

    User validateCredentials(CredentialsDto credentialsDto);

    List<UserResponseDto> getAllUsers();

    UserResponseDto createUser(UserRequestDto userRequestDto);

    UserResponseDto getUser(String username);

    UserResponseDto updateUser(String username, UserRequestDto userRequestDto);

    UserResponseDto deleteUser(String username, CredentialsDto credentialsDto);

    void followUser(String username, CredentialsDto credentialsDto);

    void unfollowUser(String username, CredentialsDto credentialsDto);

    List<UserResponseDto> getFollowers(String username);

    List<UserResponseDto> getFollowing(String username);

    List<TweetResponseDto> getUserFeed(String username);

    List<TweetResponseDto> getMentionedTweetsByUsername(String username);
	
	List<TweetResponseDto> getTweetsByUsername(String username);
}
