import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BasicUserDto } from './basic-user.dto';

export interface TeamDto {
  id?: number;
  name: string;
  description: string;
  teammates: BasicUserDto[];
  projectCount: number;
}

@Injectable({
  providedIn: 'root'
})
export class TeamService {
  private readonly API_URL = 'http://localhost:8080/company';

  constructor(private http: HttpClient) { }

  getTeamsByCompanyId(companyId: number): Observable<TeamDto[]> {
    return this.http.get<TeamDto[]>(`${this.API_URL}/${companyId}/teams`);
  }

  postTeamToCompany(companyId: number, team: TeamDto): Observable<TeamDto> {
    return this.http.post<TeamDto>(`${this.API_URL}/${companyId}/teams`, team);
  }
}
