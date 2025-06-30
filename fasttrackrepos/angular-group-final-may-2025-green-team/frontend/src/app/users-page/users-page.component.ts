import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { FullUserDto } from '../services/full-user.dto';
import { UserRequestDto } from '../services/user-request.dto';
import { SharedDataService } from '../shared-data.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-users-page',
  templateUrl: './users-page.component.html',
  styleUrls: ['./users-page.component.css']
})
export class UsersPageComponent implements OnInit {

  users: FullUserDto[] = [];
  companyId: number | null = null;

  private companySub!: Subscription;

  showUserOverlay = false;

  userForm!: FormGroup;
  dropdownOpen = false;

  constructor(private fb: FormBuilder, private userService: UserService, private sharedDataService: SharedDataService) { }

  ngOnInit() {
    this.companySub = this.sharedDataService.selectedCompanyId$.subscribe(id => {
      console.log("received company id:", id)
      this.companyId = id;
      if (id !== null) {
        this.fetchUsers(id);
      } else {
        console.error("Invalid Company ID")
      }
    });
    // this.companyId = this.sharedDataService.getSelectedCompanyId();
    // if (this.companyId !== null) {
    //   this.fetchUsers(this.companyId);
    // } else {
    //   console.error('Invalid/Null Company ID', this.companyId);
    // }

    this.initForm();
  }


  ngOnDestroy() {
    this.companySub?.unsubscribe();
  }

  fetchUsers(companyId: number) {
    this.userService.getUsersByCompanyId(companyId).subscribe({
      next: (data) => {
        this.users = data;
      },
      error: (err) => {
        console.error('Error fetching users: ', err);
      }
    });
  }

  initForm() {
    this.userForm = this.fb.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      phone: [''],
      password: ['', Validators.required],
      confirmPassword: ['', Validators.required],
      adminRole: [null, Validators.required]
    }, {
      validators: this.passwordMatchValidator
    });
  }

  passwordMatchValidator = (form: FormGroup) => {
    const pw = form.get('password')!.value;
    const cpw = form.get('confirmPassword')!.value;
    return pw === cpw ? null : { passwordMismatch: true };
  };

  toggleDropdown() {
    this.dropdownOpen = !this.dropdownOpen;
  }

  selectRole(value: boolean) {
    this.userForm.patchValue({ adminRole: value });
    this.dropdownOpen = false;
  }

  submitNewUser() {
    console.log('Submit called');
    console.log('Form Valid:', this.userForm.valid);
    console.log('Form Value:', this.userForm.value);

    if (this.userForm.valid) {
      const userReq: UserRequestDto = {
        credentials: {
          username: this.userForm.value.email,
          email: this.userForm.value.email,
          password: this.userForm.value.password
        },
        profile: {
          firstName: this.userForm.value.firstName,
          lastName: this.userForm.value.lastName,
          email: this.userForm.value.email,
          phone: this.userForm.value.phone
        },
        admin: this.userForm.value.adminRole
      };

      if (this.companyId !== null) {
        this.userService.addUserToCompany(this.companyId, userReq).subscribe({
          next: (newUser) => {
            this.users.push(newUser);
            this.closeAddUser();
            this.userForm.reset();
          },
          error: (err) => {
            console.error('Failed to create user: ', err);
          }
        });
      } else {
        this.userForm.markAllAsTouched();
      }
    } else {
      console.error('Invalid company ID')
    }
  }

  // Methods for displaying Modal
  openAddUser() {
    this.showUserOverlay = true;
  }

  closeAddUser() {
    this.showUserOverlay = false;
  }

}
