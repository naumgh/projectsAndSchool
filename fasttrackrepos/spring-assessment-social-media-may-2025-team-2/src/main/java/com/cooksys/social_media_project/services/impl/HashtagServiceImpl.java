package com.cooksys.social_media_project.services.impl;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.entities.Hashtag;
import com.cooksys.social_media_project.entities.Tweet;
import com.cooksys.social_media_project.exceptions.NotFoundException;
import com.cooksys.social_media_project.mappers.HashtagMapper;
import com.cooksys.social_media_project.mappers.TweetMapper;
import com.cooksys.social_media_project.repositories.HashtagRepository;
import com.cooksys.social_media_project.services.HashtagService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class HashtagServiceImpl implements HashtagService {

	private final HashtagRepository hashtagRepository;
	private final HashtagMapper hashtagMapper;
	private final TweetMapper tweetMapper;

	// Retrieves all hashtags
	@Override
	public List<HashtagDto> getAllTags() {
		List<Hashtag> tags = hashtagRepository.findAll();
		return hashtagMapper.entitiesToDtos(tags);
	}

	// Returns all tweets with the given hashtag label
	@Override
	public List<TweetResponseDto> getTweetsByHashtag(String label) {
		Hashtag hashtag = hashtagRepository.findByLabelIgnoreCase(label)
				.orElseThrow(() -> new NotFoundException("No hashtag found with label: #" + label));

		List<Tweet> nonDeletedTweets = new ArrayList<>();

		// Add non-deleted tweets to arraylist
		for (Tweet tweet : hashtag.getTweets()) {
			nonDeletedTweets.add(tweet);
		}

		// Sorts list in a reverse chronological order
		nonDeletedTweets.sort((t1, t2) -> t2.getPosted().compareTo(t1.getPosted()));

		return tweetMapper.entitiesToResponseDtos(nonDeletedTweets);
	}

}
