package com.cooksys.groupfinal.controllers;

import java.util.Set;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.cooksys.groupfinal.dtos.CompanyDto;
import com.cooksys.groupfinal.dtos.AnnouncementDto;
import com.cooksys.groupfinal.dtos.BasicUserDto;
import com.cooksys.groupfinal.dtos.FullUserDto;
import com.cooksys.groupfinal.dtos.ProjectDto;
import com.cooksys.groupfinal.dtos.TeamDto;
import com.cooksys.groupfinal.dtos.UserRequestDto;
import com.cooksys.groupfinal.services.AnnouncementService;
import com.cooksys.groupfinal.services.CompanyService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/company")
@RequiredArgsConstructor
public class CompanyController {

    private final CompanyService companyService;

    @GetMapping("/{id}/users")
    public Set<FullUserDto> getAllUsers(@PathVariable Long id,
            @RequestParam(defaultValue = "false") boolean onlyActive) {
        return companyService.getAllUsers(id, onlyActive);
    }

    @PostMapping("/{id}/users")
    @ResponseStatus(HttpStatus.CREATED)
    public FullUserDto addUser(@PathVariable Long id, @RequestBody UserRequestDto uRequestDto) {
        return companyService.addUser(id, uRequestDto);
    }

    @GetMapping("/{id}/announcements")
    public Set<AnnouncementDto> getAllAnnouncements(@PathVariable Long id) {
        return companyService.getAllAnnouncements(id);
    }

    @PostMapping("/{id}/announcements")
    @ResponseStatus(HttpStatus.CREATED)
    public AnnouncementDto addAnnouncement(@PathVariable Long id, @RequestBody AnnouncementDto aDto) {
        return companyService.addAnnouncement(id, aDto);
    }

    @DeleteMapping("/{companyId}/announcements/{announcementId}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteAnnouncement(@PathVariable Long companyId, @PathVariable Long announcementId) {
        companyService.deleteAnnouncement(companyId, announcementId);
    }

    // @GetMapping("/{id}/teams")
    // public Set<TeamDto> getAllTeams(@PathVariable Long id) {
    // return companyService.getAllTeams(id);
    // }

    @GetMapping("/{companyId}/teams")
    public Set<TeamDto> getCompanyTeams(@PathVariable Long companyId) {
        return companyService.getCompanyTeams(companyId);
    }

    // post mappings
    @PostMapping("/{companyId}/teams")
    public TeamDto postTeamToCompany(@PathVariable Long companyId, @RequestBody TeamDto teamDto) {
        return companyService.postTeamToCompany(companyId, teamDto);
    }

    @DeleteMapping("/{companyId}/teams/{teamId}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void removeTeam(@PathVariable Long companyId, @PathVariable Long teamId) {
        companyService.removeTeam(companyId, teamId);
    }

    @GetMapping("/{companyId}/teams/{teamId}/projects")
    public Set<ProjectDto> getAllProjects(@PathVariable Long companyId, @PathVariable Long teamId) {
        return companyService.getAllProjects(companyId, teamId);
    }

    // new routes because we need to get companies that exist in the db
    @GetMapping("/{id}")
    public CompanyDto getCompanyById(@PathVariable Long id) {
        return companyService.getCompanyById(id);
    }

    @GetMapping()
    public Set<CompanyDto> getAllCompanies() {
        return companyService.getAllCompanies();
    }

    @GetMapping("/user/{userId}")
    public Set<CompanyDto> getMethodName(@PathVariable Long userId) {
        return companyService.getCompaniesByUser(userId);
    }

}
