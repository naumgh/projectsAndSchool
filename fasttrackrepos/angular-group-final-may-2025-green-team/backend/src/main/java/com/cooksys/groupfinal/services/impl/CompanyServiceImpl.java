package com.cooksys.groupfinal.services.impl;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import org.springframework.stereotype.Service;

import com.cooksys.groupfinal.dtos.AnnouncementDto;
import com.cooksys.groupfinal.dtos.BasicUserDto;
import com.cooksys.groupfinal.dtos.FullUserDto;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.dtos.UserRequestDto;
import com.cooksys.groupfinal.entities.Announcement;
import com.cooksys.groupfinal.entities.Company;
import com.cooksys.groupfinal.entities.Project;
import com.cooksys.groupfinal.entities.Team;
import com.cooksys.groupfinal.entities.User;
import com.cooksys.groupfinal.exceptions.BadRequestException;
import com.cooksys.groupfinal.exceptions.NotFoundException;
import com.cooksys.groupfinal.mappers.AnnouncementMapper;
import com.cooksys.groupfinal.mappers.ProjectMapper;
import com.cooksys.groupfinal.mappers.TeamMapper;
import com.cooksys.groupfinal.mappers.FullUserMapper;
import com.cooksys.groupfinal.repositories.AnnouncementRepository;
import com.cooksys.groupfinal.repositories.CompanyRepository;
import com.cooksys.groupfinal.repositories.TeamRepository;
import com.cooksys.groupfinal.repositories.UserRepository;
import com.cooksys.groupfinal.services.CompanyService;
import com.cooksys.groupfinal.dtos.CompanyDto;
import com.cooksys.groupfinal.mappers.CompanyMapper;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class CompanyServiceImpl implements CompanyService {

	private final CompanyRepository companyRepository;
	private final TeamRepository teamRepository;
	private final UserRepository userRepository;
	private final AnnouncementRepository announcementRepository;

	private final FullUserMapper fullUserMapper;
	private final AnnouncementMapper announcementMapper;
	private final TeamMapper teamMapper;
	private final ProjectMapper projectMapper;
	private final CompanyMapper companyMapper;

	private Company findCompany(Long id) {
		Optional<Company> company = companyRepository.findById(id);
		if (company.isEmpty()) {
			throw new NotFoundException("A company with the provided id does not exist.");
		}
		return company.get();
	}

	private Team findTeam(Long id) {
		Optional<Team> team = teamRepository.findById(id);
		if (team.isEmpty()) {
			throw new NotFoundException("A team with the provided id does not exist.");
		}
		return team.get();
	}

	private User findUser(Long id) {
		Optional<User> user = userRepository.findById(id);
		if (user.isEmpty()) {
			throw new NotFoundException("A user with the provided id does not exist.");
		}
		return user.get();
	}

	private Announcement findAnnouncement(Long id) {
		Optional<Announcement> announcement = announcementRepository.findById(id);
		if (announcement.isEmpty()) {
			throw new NotFoundException("An announcement with the provided id does not exist.");
		}
		return announcement.get();
	}

	@Override
	public Set<FullUserDto> getAllUsers(Long id, boolean onlyActive) {
		// Company company = findCompany(id);
		// Set<User> filteredUsers = new HashSet<>();
		// company.getEmployees().forEach(filteredUsers::add);
		// filteredUsers.removeIf(user -> !user.isActive());
		// return fullUserMapper.entitiesToFullUserDtos(filteredUsers);
		Company company = findCompany(id);
		Set<User> users = new HashSet<>(company.getEmployees());
		if (onlyActive) {
			users.removeIf(user -> !user.isActive());
		}
		return fullUserMapper.entitiesToFullUserDtos(users);
	}

	@Override
	public Set<AnnouncementDto> getAllAnnouncements(Long id) {
		Company company = findCompany(id);
		List<Announcement> sortedList = new ArrayList<Announcement>(company.getAnnouncements());
		sortedList.sort(Comparator.comparing(Announcement::getDate).reversed());
		Set<Announcement> sortedSet = new HashSet<Announcement>(sortedList);
		return announcementMapper.entitiesToDtos(sortedSet);
	}

	// @Override
	// public Set<TeamDto> getAllTeams(Long id) {
	// Company company = findCompany(id);
	// return teamMapper.entitiesToDtos(company.getTeams());
	// }

	@Override
	public Set<ProjectDto> getAllProjects(Long companyId, Long teamId) {
		Company company = findCompany(companyId);
		Team team = findTeam(teamId);
		if (!company.getTeams().contains(team)) {
			throw new NotFoundException(
					"A team with id " + teamId + " does not exist at company with id " + companyId + ".");
		}

		team.getProjects().size();

		Set<Project> filteredProjects = new HashSet<>();

		System.out.println("---- DEBUG LOG ----");
		System.out.println("Team ID: " + teamId + ", Total projects: " + filteredProjects.size());
		for (Project p : filteredProjects) {
			System.out.println("Project: " + p.getName() + ", Active: " + p.isActive());
		}

		team.getProjects().forEach(filteredProjects::add);
		//filteredProjects.removeIf(project -> !project.isActive());

		System.out.println("After filtering, active projects count: " + filteredProjects.size());
		System.out.println("-------------------");

		return projectMapper.entitiesToDtos(filteredProjects);
	}

	@Override
	public Set<TeamDto> getCompanyTeams(Long companyId) {
		Company company = findCompany(companyId);
		return teamMapper.entitiesToDtos(company.getTeams());
	}

	@Override
	public TeamDto postTeamToCompany(Long companyId, TeamDto teamDto) {
		Company company = companyRepository.findById(companyId)
				.orElseThrow(() -> new NotFoundException("Company with ID " + companyId + " does not exist."));
		Team team = teamMapper.dtoToEntity(teamDto);
		team.setCompany(company);
		team = teamRepository.save(team);
		return teamMapper.entityToDto(team);
	}

	@Override
	public FullUserDto addUser(Long id, UserRequestDto uRequestDto) {
		Company company = findCompany(id);

		User user = fullUserMapper.requestDtoToEntity(uRequestDto);
		user.getCompanies().add(company);

		return fullUserMapper.entityToFullUserDto(userRepository.saveAndFlush(user));

	}

	@Override
	public AnnouncementDto addAnnouncement(Long id, AnnouncementDto aDto) {
		Company company = findCompany(id);
		User author = findUser(aDto.getAuthor().getId());

		Announcement announcement = announcementMapper.dtoToEntity(aDto);
		announcement.setCompany(company);
		announcement.setAuthor(author);

		return announcementMapper.entityToDto(announcementRepository.saveAndFlush(announcement));
	}

	@Override
	public void removeTeam(Long companyId, Long teamId) {
		Company company = findCompany(companyId);
		Team team = findTeam(teamId);

		company.getTeams().remove(team);
		team.setCompany(null);

		team.getTeammates().clear();
		team.getProjects().clear();

		teamRepository.delete(team);
	}

	@Override
	public void deleteAnnouncement(Long companyId, Long announcementId) {
		Company company = findCompany(companyId);
		Announcement announcement = findAnnouncement(announcementId);

		if (!announcement.getCompany().getId().equals(company.getId())) {
			throw new BadRequestException("Announcement does not belong to company");
		}

		company.getAnnouncements().remove(announcement);
		announcement.setCompany(null);
		announcement.setAuthor(null);

		announcementRepository.delete(announcement);
	}

	@Override
	public Set<CompanyDto> getAllCompanies() {
		return companyMapper.entitiesToDtos(new HashSet<>(companyRepository.findAll()));
	}

	@Override
	public CompanyDto getCompanyById(Long id) {
		return companyMapper.entityToDto(
				companyRepository.findById(id)
						.orElseThrow(() -> new NotFoundException("Company with ID " + id + " not found.")));
	}

	@Override
	public Set<CompanyDto> getCompaniesByUser(Long user) {
		return companyMapper.entitiesToDtos(companyRepository.findByEmployees_Id(user));
	}

}
