package com.cooksys.social_media_project.services.impl;


import org.springframework.stereotype.Service;

import com.cooksys.social_media_project.repositories.HashtagRepository;
import com.cooksys.social_media_project.repositories.UserRepository;
import com.cooksys.social_media_project.services.ValidateService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ValidateServiceImpl implements ValidateService {
	
	private final HashtagRepository hashtagRepository;
	private final UserRepository userRepository;

	public boolean tagExists(String label) {
		return hashtagRepository.existsByLabelIgnoreCase(label);
	}

    public boolean usernameExists(String username) {
		return !userRepository.findByCredentials_Username(username).isEmpty();

	}

    public boolean usernameAvailable(String username) {
		return (userRepository.findByCredentials_Username(username).isEmpty() || userRepository.findByCredentials_Username(username).get().isDeleted());
	}

}
