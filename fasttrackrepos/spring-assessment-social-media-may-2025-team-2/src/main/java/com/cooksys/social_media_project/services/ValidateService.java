package com.cooksys.social_media_project.services;

public interface ValidateService {

    boolean tagExists(String label);

    boolean usernameExists(String username);

    boolean usernameAvailable(String username);

}
