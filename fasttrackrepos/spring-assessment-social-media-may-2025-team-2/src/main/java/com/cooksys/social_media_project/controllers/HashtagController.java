package com.cooksys.social_media_project.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.services.HashtagService;

import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@RequestMapping("tags")
public class HashtagController {

	private final HashtagService hashtagService;
	
	@GetMapping
	public List<HashtagDto> getAllTags(){
		return hashtagService.getAllTags();
	}
	
	@GetMapping("/{label}")
	public List<TweetResponseDto> getTweetsByHashtag(@PathVariable String label) {
		return hashtagService.getTweetsByHashtag(label);
	}
	
}
