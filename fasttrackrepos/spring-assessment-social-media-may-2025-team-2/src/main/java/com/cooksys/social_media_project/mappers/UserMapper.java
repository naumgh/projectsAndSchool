package com.cooksys.social_media_project.mappers;

import java.util.List;

import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.MappingTarget;
import org.mapstruct.NullValuePropertyMappingStrategy;

import com.cooksys.social_media_project.dtos.UserRequestDto;
import com.cooksys.social_media_project.dtos.UserResponseDto;
import com.cooksys.social_media_project.entities.User;

@Mapper(componentModel = "spring", uses = {CredentialsMapper.class, ProfileMapper.class },
	nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)
public interface UserMapper {
	
	@Mapping(source = "credentials.username", target = "username")
	UserResponseDto entityToDto(User user);
	
	User dtoToEntity(UserRequestDto dto);
	
	List<UserResponseDto> entitiesToDtos(List<User> users);
	
	void updateEntityFromDto(UserRequestDto dto, @MappingTarget User user);
	
}
