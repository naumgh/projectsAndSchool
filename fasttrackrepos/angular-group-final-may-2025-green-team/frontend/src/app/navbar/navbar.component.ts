import { Component, OnInit } from '@angular/core';
import { SharedDataService } from '../shared-data.service';
import { BasicUserDto } from '../services/basic-user.dto';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent implements OnInit{
  admin: boolean = false;
  user: BasicUserDto | null = null;

  swirlSrc = 'assets/blue-swirl.png';

  constructor(private sharedDataService: SharedDataService) {}

  ngOnInit(): void {
    this.admin = this.sharedDataService.getIsAdmin();
    console.log(this.admin);
    this.user = this.sharedDataService.getUser();
    console.log(this.user);
  }

  onHover(hovering: boolean) {
    this.swirlSrc = hovering
      ? 'assets/gold-swirl.png'
      : 'assets/blue-swirl.png';
  }
}
