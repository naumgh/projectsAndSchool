package com.cooksys.social_media_project.controllers;

import java.util.List;


import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.cooksys.social_media_project.dtos.ContextDto;
import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.TweetRequestDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.services.TweetService;

import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@RequestMapping("tweets")
public class TweetController {

	private final TweetService tweetService;
	
	@GetMapping
	public List<TweetResponseDto> getAllTweets() {
		return tweetService.getAllTweets();
	}
	
	@PostMapping
	@ResponseStatus(HttpStatus.CREATED)
	public TweetResponseDto createTweet(@RequestBody TweetRequestDto tweetRequestDto) {
		return tweetService.createTweet(tweetRequestDto);
	}
	
	@GetMapping("/{id}")
	public TweetResponseDto getTweetById(@PathVariable Long id) {
		return tweetService.getTweetById(id);
	}
	
	@DeleteMapping("/{id}")
	public TweetResponseDto deleteTweet(@PathVariable Long id) {
		return tweetService.deleteTweet(id);
	}
	
	@GetMapping("/{id}/tags")
	public List<HashtagDto> getTagsByTweetId(@PathVariable Long id) {
		return tweetService.getTagsByTweetId(id);
	}
	
	@PostMapping("/{id}/like")
	@ResponseStatus(HttpStatus.NO_CONTENT)
	public void likeTweet(@PathVariable Long id, @RequestBody CredentialsDto credentials) {
		tweetService.likeTweet(id, credentials);
	}
	
	@PostMapping("/{id}/reply")
	public TweetResponseDto replyToTweet(@PathVariable Long id, @RequestBody TweetRequestDto tweetRequestDto) {
		return tweetService.replyToTweet(id, tweetRequestDto);	
	}
	
	@PostMapping("/{id}/repost")
	public TweetResponseDto tweetRepost(@PathVariable Long id, @RequestBody CredentialsDto credentials) {
		return tweetService.tweetRepost(id, credentials);
	}
	
	@GetMapping("/{id}/mentions")
	public List<UserResponseDto> getMentions(@PathVariable Long id){
		return tweetService.getMentionsFromTweet(id);
	}
	
	@GetMapping("/{id}/reposts")
	public List<TweetResponseDto>getReposts(@PathVariable Long id){
		return tweetService.getRepostsOfTweet(id);
	}
	
	@GetMapping("/{id}/replies")
	public List<TweetResponseDto> getRepliesToTweet(@PathVariable Long id){
		return tweetService.getRepliesToTweet(id);
	}
	
	@GetMapping("/{id}/likes")
	public List<UserResponseDto> getLikes(@PathVariable Long id){
		return tweetService.getLikes(id);
	}
	
	@GetMapping("/{id}/context")
	public ContextDto getTweetContext(@PathVariable Long id) {
	    return tweetService.getContext(id);
	}
	
}
