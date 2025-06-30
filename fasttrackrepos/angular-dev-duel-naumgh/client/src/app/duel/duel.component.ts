import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/user.service';
import { CommonModule } from '@angular/common'; 
import { ProfileCardComponent } from '../components/profile-card/profile-card.component';
import { TextInputComponent } from '../components/text-input/text-input.component';

@Component({
  standalone: true,
  selector: 'app-duel',
  templateUrl: './duel.component.html',
  styleUrls: ['./duel.component.css'],
  imports: [CommonModule, ProfileCardComponent, TextInputComponent],
})
export class DuelComponent implements OnInit {
  usernameOne: string = ""
  usernameTwo: string = ""
  profileOne: any = null;
  profileTwo: any = null;
  error: string = "";

  constructor(private userService: UserService) { }

  ngOnInit(): void {
  }

  receiveUsernameOne(valueEmitted: string) {
    this.usernameOne = valueEmitted;
  }

  receiveUsernameTwo(valueEmitted: string) {
    this.usernameTwo = valueEmitted;
  }

  
  onSubmit() {
    this.winner= null;
    this.userService.duelUsers(this.usernameOne, this.usernameTwo)
    .then((data) => {
    if (!Array.isArray(data) || data.length < 2) {
      this.profileOne = null;
      this.profileTwo = null;
      this.error = "Not enough data received.";
      return;
    }
    this.profileOne = data[0];
    this.profileTwo = data[1];
    this.error = "";

  const score1 = this.calculateScore(this.profileOne);
  const score2 = this.calculateScore(this.profileTwo);

  if (score1 > score2) {
    this.winner = 'Player 1';
  } else if (score2 > score1) {
    this.winner = 'Player 2';
  }else if (score1 === score2) {
    this.winner = 'It\'s a tie!';
  }

  })
  .catch((err) => {
  this.profileOne = null;
  this.profileTwo = null;
  this.winner = null;

  console.error('FULL ERROR OBJECT:', err);

  const tips = err?.error?.tips;
  const message = err?.error?.message;

  this.error = tips || message || "An unknown error occurred.";
});
  }
  winner: 'Player 1' | 'Player 2' | 'It\'s a tie!' | null = null;

  calculateScore(profile: any): number {
  //user must automatically lose if their favorite language is javascript
  if (profile['favorite-language'] === 'JavaScript') {
    return -99999;
  }
  return (
    profile.followers +
    profile.following +
    profile['public-repos'] +
    profile['total-stars'] +
    profile['highest-starred']+
    profile['perfect-repos'] +
    profile['titles'].length
  );

  }

}
