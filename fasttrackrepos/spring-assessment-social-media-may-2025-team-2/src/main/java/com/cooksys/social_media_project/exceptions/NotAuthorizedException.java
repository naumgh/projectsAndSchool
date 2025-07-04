package com.cooksys.social_media_project.exceptions;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@AllArgsConstructor
@Getter
@Setter
public class NotAuthorizedException extends RuntimeException {

    private static final long serialVersionUID = 1487813305L;    

    private String message;
    
}
