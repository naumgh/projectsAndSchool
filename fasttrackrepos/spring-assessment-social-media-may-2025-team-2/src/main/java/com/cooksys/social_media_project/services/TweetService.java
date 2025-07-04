package com.cooksys.social_media_project.services;

import java.util.List;

import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.ContextDto;
import com.cooksys.social_media_project.dtos.TweetRequestDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.entities.Tweet;

public interface TweetService {

	Tweet getTweet(Long id);
	
	List<TweetResponseDto> getAllTweets();

	TweetResponseDto createTweet(TweetRequestDto tweetRequestDto);

	TweetResponseDto getTweetById(Long id);
	
	List<UserResponseDto> getMentionsFromTweet(Long id);
	
	List<TweetResponseDto> getRepostsOfTweet(Long id);

	List<TweetResponseDto> getRepliesToTweet(Long id);
	
	ContextDto getContext(Long id);
	
	List<UserResponseDto> getLikes(Long id);

	TweetResponseDto deleteTweet(Long id);

	List<HashtagDto> getTagsByTweetId(Long id);

	void likeTweet(Long id, CredentialsDto credentials);

	TweetResponseDto replyToTweet(Long id, TweetRequestDto tweetRequestDto);

	TweetResponseDto tweetRepost(Long id, CredentialsDto credentials);
	
	
}
