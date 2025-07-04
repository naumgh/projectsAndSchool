package com.cooksys.social_media_project.mappers;

import org.mapstruct.Mapper;

import com.cooksys.social_media_project.dtos.ProfileDto;
import com.cooksys.social_media_project.entities.Profile;

@Mapper(componentModel = "spring")
public interface ProfileMapper {

	ProfileDto entityToDto(Profile profile);
	
	Profile dtoToEntity(ProfileDto dto);
	
}
