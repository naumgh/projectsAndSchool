package com.cooksys.social_media_project.mappers;

import org.mapstruct.Mapper;

import com.cooksys.social_media_project.dtos.CredentialsDto;
import com.cooksys.social_media_project.entities.Credentials;

@Mapper(componentModel = "spring")
public interface CredentialsMapper {

	CredentialsDto entityToDto(Credentials credentials);
	
	Credentials dtoToEntity(CredentialsDto dto);
	
}
