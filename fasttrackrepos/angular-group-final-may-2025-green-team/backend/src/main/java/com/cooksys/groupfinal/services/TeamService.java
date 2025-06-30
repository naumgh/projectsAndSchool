package com.cooksys.groupfinal.services;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.dtos.ProjectDto;

public interface TeamService {
    TeamDto patchTeamProject(Long teamId, ProjectDto projectDto);

    ProjectDto addProject(Long id, ProjectDto projectDto);

    void deleteProject(Long companyId, Long projectId);

}
