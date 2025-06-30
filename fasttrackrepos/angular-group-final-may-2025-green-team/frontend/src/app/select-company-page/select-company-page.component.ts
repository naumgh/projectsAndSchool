import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SharedDataService } from '../shared-data.service';
import { BasicUserDto } from '../services/basic-user.dto';
import { Subscription } from 'rxjs';

// company interface
interface Company {
  id: number;
  name: string
}

@Component({
  selector: 'app-select-company-page',
  templateUrl: './select-company-page.component.html',
  styleUrls: ['./select-company-page.component.css']
})
export class SelectCompanyPageComponent implements OnInit {
  // companies to display and id
  companies: Company[] = [];
  selectedCompany: number | null = null;

  // User that is logged in
  userId!: number | undefined;

  // Admin status
  isAdmin: boolean = false;

  private userSub!: Subscription;

  selectedCompanyName: string = '';

  constructor(private router: Router, private sharedDataService: SharedDataService) { }

  ngOnInit(): void {
    this.userSub = this.sharedDataService.user$.subscribe((user: BasicUserDto | null) => {
      if (user) {
        this.userId = user.id;
        this.isAdmin = user.admin;
        console.log('User updated:', user);
        console.log('Admin status updated:', this.isAdmin)

        // Fetch companies on user change
        this.isAdmin ? this.fetchCompaniesAdmin() : this.fetchCompaniesUser();
      }
    })

    // this.isAdmin = this.sharedDataService.getIsAdmin();
    // this.userId = this.sharedDataService.getUser()?.id;

    // if (this.isAdmin) {
    //   this.fetchCompaniesAdmin();
    // } else {
    //   this.fetchCompaniesUser();
    // }
  }

  fetchCompaniesAdmin() {
    fetch('http://localhost:4200/company')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
      })
      .then((data: Company[]) => {
        this.companies = data;
      })
      .catch(err => {
        console.error('Error fetching companies:', err);
      });
  }

  fetchCompaniesUser() {
    // Validate user ID
    if (this.userId === undefined) {
      console.error('Invalid user ID');
      return;
    }

    // fetch corresponding companies
    fetch(`http://localhost:4200/company/user/${this.userId}`)
      .then(res => res.json())
      .then((data: Company[]) => {
        console.log('Cmpanies fetched:', data);
        this.companies = data;
      })
      .catch(err => {
        console.error('Error fetching companies by user:', err);
      })


  }

  onCompanyChange(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    this.selectedCompany = selectElement.value ? +selectElement.value : null;
    console.log('Selected company changed:', this.selectedCompany);
  }

  submitCompany(): void {
    if (this.selectedCompany !== null && this.selectedCompany !== undefined) {
      this.sharedDataService.setSelectedCompanyId(this.selectedCompany);
      this.router.navigate(['/announcements']);
      console.log('selectedCompanyId:', this.sharedDataService.getSelectedCompanyId())
    } else {
      alert('Please select a company')
    }
  }

}
