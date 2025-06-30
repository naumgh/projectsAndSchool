import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { BasicUserDto } from './services/basic-user.dto';

@Injectable({
  providedIn: 'root'
})
export class SharedDataService {
  private readonly COMPANY_STORAGE_KEY = 'selectedCompanyId';
  private readonly ADMIN_STORAGE_KEY = 'isAdmin';
  private readonly USER_STORAGE_KEY = 'user'

  // Stores selected company
  private _selectedCompanyId = new BehaviorSubject<number | null>(
    localStorage.getItem(this.COMPANY_STORAGE_KEY) ? +localStorage.getItem(this.COMPANY_STORAGE_KEY)! : null
  );
  selectedCompanyId$: Observable<number | null> = this._selectedCompanyId.asObservable();

  // Stores userdto
  private _user = new BehaviorSubject<BasicUserDto | null>(
    localStorage.getItem(this.USER_STORAGE_KEY) ? JSON.parse(localStorage.getItem(this.USER_STORAGE_KEY)!) : null
  );
  user$: Observable<BasicUserDto | null> = this._user.asObservable();

  // Stores admin status
  private _isAdmin = new BehaviorSubject<boolean>(
    localStorage.getItem(this.ADMIN_STORAGE_KEY) === 'true'
  );
  isAdmin$: Observable<boolean> = this._isAdmin.asObservable();

  constructor() { }

  // User Getter and setter
  getUser(): BasicUserDto | null {
    return this._user.getValue();
  }

  setUser(user: BasicUserDto) {
    localStorage.setItem(this.USER_STORAGE_KEY, JSON.stringify(user));
    this._user.next(user);
    this.setIsAdmin();
  }

  // isAdmin Getters and Setters
  setIsAdmin(): void {
    const user = this.getUser();
    const isAdmin = user?.admin ?? false;
    localStorage.setItem(this.ADMIN_STORAGE_KEY, String(isAdmin));
    this._isAdmin.next(isAdmin);
  }

  getIsAdmin(): boolean {
    return this._isAdmin.getValue();
  }

  // Update company id
  setSelectedCompanyId(newId: number): void {
    localStorage.setItem(this.COMPANY_STORAGE_KEY, newId.toString());
    this._selectedCompanyId.next(newId);
  }

  // Get company id
  getSelectedCompanyId(): number | null {
    return this._selectedCompanyId.getValue();
  }
}
 