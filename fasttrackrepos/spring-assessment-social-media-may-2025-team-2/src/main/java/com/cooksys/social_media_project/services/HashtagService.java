package com.cooksys.social_media_project.services;

import java.util.List;

import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;

public interface HashtagService {
	
	List<HashtagDto> getAllTags();

	List<TweetResponseDto> getTweetsByHashtag(String label);
}
