package com.cooksys.social_media_project.dtos;

import java.sql.Timestamp;

import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@Getter
@Setter
public class UserResponseDto {

    private String username;

    private ProfileDto profile;

    private Timestamp joined;
    
}
