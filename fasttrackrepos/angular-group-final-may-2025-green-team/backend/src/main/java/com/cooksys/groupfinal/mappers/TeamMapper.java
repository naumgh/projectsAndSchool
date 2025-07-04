package com.cooksys.groupfinal.mappers;

import java.util.Set;

import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.entities.Team;

@Mapper(componentModel = "spring", uses = { BasicUserMapper.class })
public interface TeamMapper {
	
	@Mapping(target = "projectCount", expression = "java(team.getProjects().size())")
  TeamDto entityToDto(Team team);

  Set<TeamDto> entitiesToDtos(Set<Team> teams);

  Team dtoToEntity(TeamDto teamDto);

}