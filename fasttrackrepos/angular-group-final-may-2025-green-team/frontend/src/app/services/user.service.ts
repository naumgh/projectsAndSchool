import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BasicUserDto } from './basic-user.dto';
import { FullUserDto } from './full-user.dto';
import { UserRequestDto } from './user-request.dto';
import { CredentialsDto } from './credentials.dto';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private API_URL = 'http://localhost:8080/company';

  constructor(private http: HttpClient) { }

  getUsersByCompanyId(companyId: number): Observable<FullUserDto[]> {
    return this.http.get<FullUserDto[]>(`${this.API_URL}/${companyId}/users`);
  }

  addUserToCompany(companyId: number, user: UserRequestDto): Observable<FullUserDto> {
    return this.http.post<FullUserDto>(`${this.API_URL}/${companyId}/users`, user);
  }

  login(credentials: CredentialsDto): Observable<BasicUserDto> {
    return this.http.post<BasicUserDto>(`${this.API_URL}/login`, credentials);
  }
}
