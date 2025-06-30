package com.cooksys.groupfinal.services.impl;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import org.springframework.stereotype.Service;

import com.cooksys.groupfinal.dtos.AnnouncementDto;
import com.cooksys.groupfinal.dtos.FullUserDto;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.entities.Announcement;
import com.cooksys.groupfinal.entities.Company;
import com.cooksys.groupfinal.entities.Project;
import com.cooksys.groupfinal.entities.Team;
import com.cooksys.groupfinal.entities.User;
import com.cooksys.groupfinal.exceptions.BadRequestException;
import com.cooksys.groupfinal.exceptions.NotFoundException;
import com.cooksys.groupfinal.mappers.AnnouncementMapper;
import com.cooksys.groupfinal.mappers.FullUserMapper;
import com.cooksys.groupfinal.mappers.ProjectMapper;
import com.cooksys.groupfinal.mappers.TeamMapper;
import com.cooksys.groupfinal.repositories.CompanyRepository;
import com.cooksys.groupfinal.repositories.ProjectRepository;
import com.cooksys.groupfinal.repositories.TeamRepository;
import com.cooksys.groupfinal.services.CompanyService;
import com.cooksys.groupfinal.services.TeamService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class TeamServiceImpl implements TeamService {
    private final CompanyRepository companyRepository;
	private final TeamRepository teamRepository;
	private final FullUserMapper fullUserMapper;
	private final AnnouncementMapper announcementMapper;
	private final TeamMapper teamMapper;
	private final ProjectMapper projectMapper;
    private final ProjectRepository projectRepository;

    private Team findTeam(Long id) {
        Optional<Team> team = teamRepository.findById(id);
        if (team.isEmpty()) {
            throw new NotFoundException("A team with the provided id does not exist.");
        }
        return team.get();
    }


    @Override
    public TeamDto patchTeamProject(Long teamId, ProjectDto projectDto) {
        Team team = findTeam(teamId);
        Long projectId = projectDto.getId();
        if (projectId == null) {
            throw new NotFoundException("Project ID must be provided.");
        }

        Project project = projectRepository.findById(projectId)
                .orElseThrow(() -> new NotFoundException("Project with ID " + projectId + " does not exist."));

        project.setName(projectDto.getName());
        project.setDescription(projectDto.getDescription());
        project.setActive(projectDto.isActive());

        if (!team.getProjects().contains(project)) {
            team.getProjects().add(project);
        }

        // if (team.getProjects() == null) {
        //     team.setProjects(new HashSet<>());
        // }
        
        // team.getProjects().add(project);
        // teamRepository.save(team);

        projectRepository.save(project);
        
        return teamMapper.entityToDto(team);
    }

    private Project findProject(Long id) {
        Optional<Project> project = projectRepository.findById(id);
        if (project.isEmpty()) {
            throw new NotFoundException("A team with the provided id does not exist.");
        }
        return project.get();
    }

    @Override
    public ProjectDto addProject(Long id, ProjectDto projectDto) {
        Team team = findTeam(id);
        Project project = projectMapper.dtoToEntity(projectDto);

        project.setTeam(team);

        return projectMapper.entityToDto(projectRepository.saveAndFlush(project));
    }

    @Override
    public void deleteProject(Long id, Long projectId) {
        Team team = findTeam(id);
        Project project = findProject(projectId);

        if (!project.getTeam().getId().equals(team.getId())){
            throw new BadRequestException("Project does not belong to team");
        }

        team.getProjects().remove(project);
        project.setTeam(null);

        projectRepository.delete(project);
    }

}
