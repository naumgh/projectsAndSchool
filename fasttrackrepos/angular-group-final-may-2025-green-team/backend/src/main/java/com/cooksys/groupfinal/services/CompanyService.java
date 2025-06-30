package com.cooksys.groupfinal.services;

import java.util.Set;

import com.cooksys.groupfinal.dtos.AnnouncementDto;
import com.cooksys.groupfinal.dtos.BasicUserDto;
import com.cooksys.groupfinal.dtos.FullUserDto;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.dtos.UserRequestDto;
import com.cooksys.groupfinal.entities.Company;
import com.cooksys.groupfinal.dtos.CompanyDto;

public interface CompanyService {

	Set<FullUserDto> getAllUsers(Long id, boolean onlyActive);

	Set<AnnouncementDto> getAllAnnouncements(Long id);

	// Set<TeamDto> getAllTeams(Long id);

	Set<ProjectDto> getAllProjects(Long companyId, Long teamId);

	Set<TeamDto> getCompanyTeams(Long companyId);

	TeamDto postTeamToCompany(Long companyId, TeamDto teamDto);

	FullUserDto addUser(Long id, UserRequestDto uRequestDto);

	AnnouncementDto addAnnouncement(Long id, AnnouncementDto aDto);

	void removeTeam(Long companyId, Long teamId);

	void deleteAnnouncement(Long companyId, Long announcementId);

	Set<CompanyDto> getAllCompanies();

	// Get all companies associated with user
	Set<CompanyDto> getCompaniesByUser(Long user);

	CompanyDto getCompanyById(Long id);

}
