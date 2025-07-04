package com.cooksys.social_media_project.services.impl;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import com.cooksys.social_media_project.dtos.ContextDto;
import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.TweetRequestDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.entities.Hashtag;
import com.cooksys.social_media_project.entities.Tweet;
import com.cooksys.social_media_project.entities.User;
import com.cooksys.social_media_project.exceptions.BadRequestException;
import com.cooksys.social_media_project.exceptions.NotFoundException;
import com.cooksys.social_media_project.mappers.HashtagMapper;
import com.cooksys.social_media_project.mappers.TweetMapper;
import com.cooksys.social_media_project.mappers.UserMapper;
import com.cooksys.social_media_project.repositories.HashtagRepository;
import com.cooksys.social_media_project.repositories.TweetRepository;
import com.cooksys.social_media_project.repositories.UserRepository;
import com.cooksys.social_media_project.services.TweetService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class TweetServiceImpl implements TweetService {

	private final TweetRepository tweetRepository;
	private final UserRepository userRepository;
	private final HashtagRepository hashtagRepository;
	private final TweetMapper tweetMapper;
	private final UserMapper userMapper;
	private final HashtagMapper hashtagMapper;

	// Helper method to validate credentials
	private boolean validateCredentials(CredentialsDto credentials) {
		// Ensure credentials aren't null
		if (credentials == null || credentials.getUsername() == null || credentials.getPassword() == null) {
			return false;
		}

		// Find user by credentials username and ensure it's not deleted
		Optional<User> optionalUser = userRepository
				.findByCredentials_UsernameAndDeletedFalse(credentials.getUsername());

		// Check for password match
		if (optionalUser.isPresent()) {
			// Remove optional type
			User user = optionalUser.get();
			if (user.getCredentials().getPassword().equals(credentials.getPassword())) {
				return true;
			}
		}

		return false;
	}
	
	// Helper method that returns a user based on provided credentials,
	// but also provides built-in validation in the same step
	private User getUserFromCredentials(CredentialsDto credentials) {
		if (credentials == null || credentials.getUsername() == null || credentials.getPassword() == null) {
			throw new BadRequestException("Credentials are required.");
		}

		User user = userRepository.findByCredentials_UsernameAndDeletedFalse(credentials.getUsername())
			.orElseThrow(() -> new BadRequestException("Invalid credentials or inactive user."));

		if (!user.getCredentials().getPassword().equals(credentials.getPassword())) {
			throw new BadRequestException("Invalid credentials.");
		}

		return user;
	}

	// Helper method to extract hashtags
	private List<String> extractHashtags(String content) {

		List<String> tags = new ArrayList<>();

		// Use regex to look for hashtags (or rather labels after # symbol)
		Pattern tagPattern = Pattern.compile("#(\\w+)");
		Matcher matcher = tagPattern.matcher(content);

		// Loop through matches and add to list
		while (matcher.find()) {
			String label = matcher.group(1);
			tags.add(label);
		}

		return tags;
	}

	// Helper method to extract mentions
	private List<String> extractMentions(String content) {

		List<String> mentions = new ArrayList<>();

		// Use regex to look for mentions (text after the @ symbol)
		Pattern tagPattern = Pattern.compile("@(\\w+)");
		Matcher matcher = tagPattern.matcher(content);

		// Loop through matches and add to list
		while (matcher.find()) {
			String mention = matcher.group(1);
			mentions.add(mention);
		}

		return mentions;
	}

	// getTweet(Long id) is a helper method that will check to see if tweet with
	// given id exists and is not deleted, if so it returns tweet, otherwise it throws a NotFoundException
	@Override
	public Tweet getTweet(Long id) {
		return tweetRepository.findByIdAndDeletedFalse(id).orElseThrow(() -> 
			new NotFoundException("No active tweet found with id: " + id));
	}

	@Override
	public List<TweetResponseDto> getAllTweets() {
		List<Tweet> tweets = tweetRepository.findAllByDeletedFalse(Sort.by(Sort.Direction.DESC, "posted"));
		return tweetMapper.entitiesToResponseDtos(tweets);
	}

	@Override
	public TweetResponseDto createTweet(TweetRequestDto tweetRequestDto) {

		if (tweetRequestDto.getContent() == null) {
			throw new BadRequestException("Tweet content is required but not provided.");
		}

		// Gets credentials
		CredentialsDto credentials = tweetRequestDto.getCredentials();
		// Validate credentials
		if (!validateCredentials(credentials)) {
			throw new BadRequestException("Invalid credentials or inactive user.");
		}
		// Gets tweet
		Tweet tweet = tweetMapper.requestDtoToEntity(tweetRequestDto);
		// Gets user based on credentials (we'll need to have a
		// findByCredentialsUsername or something in the UserRepository to do this
		User author = userRepository.findByCredentials_Username(credentials.getUsername()).get();

		// Sets fields
		tweet.setAuthor(author);
		tweet.setInReplyTo(null);
		tweet.setRepostOf(null);
		tweet.setDeleted(false);

		// Extract hashtags and mentions
		String content = tweet.getContent();
		List<String> hashtags = extractHashtags(content);
		List<String> mentions = extractMentions(content);

		// Process hashtags
		List<Hashtag> processedTags = new ArrayList<>();
		Timestamp timestamp = new Timestamp(System.currentTimeMillis());
		// Loop through extracted hashtag labels (from content)
		for (String label : hashtags) {
			Optional<Hashtag> optionalHashtag = hashtagRepository.findByLabelIgnoreCase(label);
			Hashtag hashtag;
			if (!optionalHashtag.isEmpty()) {
				// tag already exists, update its lastUsed
				hashtag = optionalHashtag.get();
				hashtag.setLastUsed(timestamp);
				hashtagRepository.saveAndFlush(hashtag);
			}
			else {
				// If hashtag doesn't exist in repository, create new hashtag
				hashtag = new Hashtag();
				hashtag.setLabel(label);
				hashtagRepository.saveAndFlush(hashtag);
			}
			processedTags.add(hashtag);			
		}
		tweet.setHashtags(processedTags);

		// Process mentions
		List<User> processedMentions = new ArrayList<>();
		for (String username : mentions) {
			userRepository.findByCredentials_Username(username).ifPresent(user -> {
				processedMentions.add(user);
				if (user.getMentionedIn() == null) {
					user.setMentionedIn(new ArrayList<>());
				}
				user.getMentionedIn().add(tweet);
			});
		}
		tweet.setMentions(processedMentions);

		return tweetMapper.entityToResponseDto(tweetRepository.saveAndFlush(tweet));
	}

	@Override
	public TweetResponseDto getTweetById(Long id) {
		return tweetMapper.entityToResponseDto(getTweet(id));
	}
	
	@Override
	public List<UserResponseDto> getMentionsFromTweet(Long id){
		Tweet tweet = getTweet(id);
		if(tweet.isDeleted()) {
			throw new BadRequestException("Tweet " + id + " is deleted.");
		}
		
		List<User> mentionedUsers = tweet.getMentions();
		List<User> activeMentionedUsers = new ArrayList<>();
		
		
		//deleted users should be excluded from response
		for(User user : mentionedUsers) {
			if(!user.isDeleted()) {
				activeMentionedUsers.add(user);
			}
		}
		
		return userMapper.entitiesToDtos(activeMentionedUsers);
	}
	
	@Override
	public List<TweetResponseDto>getRepostsOfTweet(Long id){
		Tweet tweet = getTweet(id);
		if(tweet.isDeleted()) {
			throw new BadRequestException("Tweet " + id + " is deleted.");
		}
		
		List<Tweet> reposts = tweetRepository.findAllByRepostOfAndDeletedFalse(tweet);
		return tweetMapper.entitiesToResponseDtos(reposts);
	}
	
	@Override
	public List<TweetResponseDto> getRepliesToTweet(Long id){
		Tweet tweet = getTweet(id);
		
		List<Tweet> replies = tweetRepository.findAllByInReplyToAndDeletedFalse(tweet);
		
		return tweetMapper.entitiesToResponseDtos(replies);
	}
	
	@Override
	public List<UserResponseDto> getLikes(Long id){
		Tweet tweet = getTweet(id);
		if(tweet.isDeleted()) {
			throw new BadRequestException("Tweet " + id + " is deleted.");
		}
		
		List<User> activeLikedUsers = new ArrayList<>();
		
		for (User user: tweet.getLikedBy()) {
			if(!user.isDeleted()) {
				activeLikedUsers.add(user);
			}
		}
		
		return userMapper.entitiesToDtos(activeLikedUsers);
	}
	
	@Override
	public TweetResponseDto deleteTweet(Long id) {
		Tweet tweetToDelete = getTweet(id);
		tweetToDelete.setDeleted(true);
		return tweetMapper.entityToResponseDto(tweetRepository.saveAndFlush(tweetToDelete));
	}

	@Override
	public List<HashtagDto> getTagsByTweetId(Long id) {
		Tweet tweet = getTweet(id);

		if (tweet.getHashtags() != null) {
			return hashtagMapper.entitiesToDtos(tweet.getHashtags());
		} else {
			return new ArrayList<>();
		}
	}

	@Override
	public void likeTweet(Long id, CredentialsDto credentials) {
		Tweet tweet = getTweet(id);
		
		// Retrieve user from repository based on credentials provided (also validates credentials)
		User user = getUserFromCredentials(credentials);
		
		// if tweet has not already been liked by user, add liked tweet to user, 
		// and user to tweet (for users who liked it)
		if (!tweet.getLikedBy().contains(user)) {
			tweet.getLikedBy().add(user);
			user.getLikedTweets().add(tweet);
		}
		
		userRepository.saveAndFlush(user);
		tweetRepository.saveAndFlush(tweet);
	}

	@Override
	public TweetResponseDto replyToTweet(Long id, TweetRequestDto tweetRequestDto) {
		// Gets tweet that we're replying to
		Tweet repliedToTweet = getTweet(id);
		
		// Creates a new tweet
		TweetResponseDto newTweetDto = createTweet(tweetRequestDto);
		Long newTweetId = newTweetDto.getId();
		
		// Gets new tweet
		Tweet newTweet = getTweet(newTweetId);
		
		// Sets inReplyTo field for new tweet
		newTweet.setInReplyTo(repliedToTweet);
		return tweetMapper.entityToResponseDto(tweetRepository.saveAndFlush(newTweet));
	}

	@Override
	public TweetResponseDto tweetRepost(Long id, CredentialsDto credentials) {
		// Gets the tweet that will be reposted
		Tweet originalTweet = getTweet(id);
		
		// Retrieves user from repository and includes credential validation 
		User user = getUserFromCredentials(credentials);
		
		if (user == null) {
			throw new BadRequestException("Credentials provided are invalid or user is inactive");
		}
		
		// Creates a new tweet for the repost, setting content to null
		Tweet repostedTweet = new Tweet();
		repostedTweet.setAuthor(user);
		repostedTweet.setRepostOf(originalTweet);
		repostedTweet.setInReplyTo(null);
		repostedTweet.setContent(null);
		repostedTweet.setDeleted(false);
		
		return tweetMapper.entityToResponseDto(tweetRepository.saveAndFlush(repostedTweet));		
	}
	@Override
	public ContextDto getContext(Long id) {
		Tweet tweet = getTweet(id);
		
		List<Tweet> before = new ArrayList<>();
		Tweet current = tweet.getInReplyTo();
		
		while (current != null) {
			if(!current.isDeleted()) {
				before.add(0, current);
			}
			current = current.getInReplyTo();
		}
		List<Tweet> after = new ArrayList<>();
		List<Tweet> process = new ArrayList<>();
		process.add(tweet);
		
		while(!process.isEmpty()) {
			Tweet parentTweet = process.remove(0);
			
			List<Tweet> replies = tweetRepository.findAllByInReplyTo(parentTweet);
			
			for(Tweet reply: replies) {
				process.add(reply);
				if(!reply.isDeleted()) {
					after.add(reply);
				}
			}
		}
		
	    after.sort((a, b) -> a.getPosted().compareTo(b.getPosted()));
	    
	    ContextDto context = new ContextDto();
	    context.setTarget(tweetMapper.entityToResponseDto(tweet));
	    context.setBefore(tweetMapper.entitiesToResponseDtos(before));
	    context.setAfter(tweetMapper.entitiesToResponseDtos(after));
		
	    return context;
	}
	

}
