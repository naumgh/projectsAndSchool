package com.cooksys.groupfinal.controllers;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.cooksys.groupfinal.dtos.ProjectDto;

import com.cooksys.groupfinal.services.TeamService;

import lombok.RequiredArgsConstructor;

import java.util.Set;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.cooksys.groupfinal.dtos.AnnouncementDto;
import com.cooksys.groupfinal.dtos.FullUserDto;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.services.CompanyService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/team-service")
@RequiredArgsConstructor
public class TeamController {

	private final TeamService teamService;

	// patch mappings
	@PatchMapping("/{teamId}/project")
	public TeamDto patchTeamProject(@PathVariable Long teamId, @RequestBody ProjectDto projectDto) {
		return teamService.patchTeamProject(teamId, projectDto);
	}

	@PostMapping("/{id}/project")
	@ResponseStatus(HttpStatus.CREATED)
	public ProjectDto addProject(@PathVariable Long id, @RequestBody ProjectDto projectDto) {
		return teamService.addProject(id, projectDto);
	}

	@DeleteMapping("/{id}/project")
	@ResponseStatus(HttpStatus.NO_CONTENT)
	public void deleteProject(@PathVariable Long id, @RequestBody Long projectId) {
		teamService.deleteProject(id, projectId);
	}

}
