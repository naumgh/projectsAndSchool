import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ProjectDto } from './project.dto';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {

  private API_URL = 'http://localhost:8080';

  constructor(private http: HttpClient) { }

  getProjectsByTeamId(companyId: number, teamId: number): Observable<ProjectDto[]> {
    return this.http.get<ProjectDto[]>(`${this.API_URL}/company/${companyId}/teams/${teamId}/projects`);
  }

  postProjectToTeam(teamId: number, project: ProjectDto): Observable<ProjectDto> {
    return this.http.post<ProjectDto>(`${this.API_URL}/team-service/${teamId}/project`, project);
  }

  patchProjectToTeam(teamId: number, project: ProjectDto): Observable<ProjectDto> {
    return this.http.patch<ProjectDto>(`${this.API_URL}/team-service/${teamId}/project`, project);
  }

}
