package com.cooksys.social_media_project.exceptions;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@AllArgsConstructor
@Getter
@Setter
public class NotFoundException extends RuntimeException {

    private static final long serialVersionUID = 5227389048L;    

    private String message;
    
}