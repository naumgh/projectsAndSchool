package com.cooksys.social_media_project.mappers;

import java.util.List;

import org.mapstruct.Mapper;
import org.mapstruct.MappingTarget;
import org.mapstruct.NullValuePropertyMappingStrategy;

import com.cooksys.social_media_project.dtos.TweetRequestDto;
import com.cooksys.social_media_project.dtos.TweetResponseDto;
import com.cooksys.social_media_project.entities.Tweet;

@Mapper(componentModel = "spring", uses = { UserMapper.class, CredentialsMapper.class },
		nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)
public interface TweetMapper {

	Tweet requestDtoToEntity(TweetRequestDto dto);
	
	TweetResponseDto entityToResponseDto(Tweet tweet);
	
	List<TweetResponseDto> entitiesToResponseDtos(List<Tweet> tweets);
	
	void updateEntityFromDto(TweetResponseDto dto, @MappingTarget Tweet tweet);
	
}
