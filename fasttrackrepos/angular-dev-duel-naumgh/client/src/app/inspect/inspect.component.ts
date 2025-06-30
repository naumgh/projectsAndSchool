import { Component, Input, OnInit } from '@angular/core';
import { UserService } from 'src/user.service';
import { ProfileCardComponent } from "../components/profile-card/profile-card.component";
import { TextInputComponent } from '../components/text-input/text-input.component';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-inspect',
  templateUrl: './inspect.component.html',
  styleUrls: ['./inspect.component.css'],
  imports: [CommonModule, ProfileCardComponent, TextInputComponent],
  standalone: true
})
export class InspectComponent implements OnInit {

  username: string = "";
  user: any = null;
  error: string = "";


  constructor(private userService: UserService) { }

  ngOnInit(): void {
  }

  receiveUsername(valueEmitted: string) {
    this.username = valueEmitted;
  }

  onSubmit() {
    this.userService.inspectUser(this.username)
    .then((data) => {
      this.user = data;
      this.error = "";
    })
    .catch((err) => {
      this.user = null;
      this.error = err.error.message || "An error occurred while fetching user data.";
    });
  }



}
