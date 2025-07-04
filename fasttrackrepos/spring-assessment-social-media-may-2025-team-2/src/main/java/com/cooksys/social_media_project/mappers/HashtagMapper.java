package com.cooksys.social_media_project.mappers;

import java.util.List;

import org.mapstruct.Mapper;
import org.mapstruct.MappingTarget;

import com.cooksys.social_media_project.dtos.HashtagDto;
import com.cooksys.social_media_project.entities.Hashtag;

@Mapper(componentModel = "spring")
public interface HashtagMapper {
	
	Hashtag dtoToEntity(HashtagDto dto);
	
	HashtagDto entityToDto(Hashtag entity);
	
	List<HashtagDto> entitiesToDtos(List<Hashtag> entities);
	
	List<Hashtag> dtosToEntities(List<HashtagDto> dtos);
	
	void updateEntityFromDto(HashtagDto dto, @MappingTarget Hashtag entity);

}
