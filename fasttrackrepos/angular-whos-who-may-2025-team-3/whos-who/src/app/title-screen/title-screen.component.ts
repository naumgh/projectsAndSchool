import { Component } from '@angular/core';
import { InputFieldComponent } from '../Components/input-field/input-field.component';
import { LinkButtonComponent } from '../Components/link-button/link-button.component';
import { SettingsComponent } from '../Components/settings/settings.component';
import { NgIf } from '@angular/common';
import { Router } from '@angular/router';
import { AudioService } from '../services/audio-service/audio.service';
import { LeaderboardComponent } from '../leaderboard/leaderboard.component';
import { PlayerService } from '../services/player.service';


@Component({
  selector: 'app-title-screen',
  imports: [NgIf, InputFieldComponent, LinkButtonComponent, SettingsComponent, LeaderboardComponent],
  templateUrl: './title-screen.component.html',
  styleUrls: ['./title-screen.component.css'],
})
export class TitleScreenComponent {
  playerName: string = '';

  showSettings: boolean = false;
  showLeaderboard = false;

  toggleLeaderboard() {
    this.showLeaderboard = !this.showLeaderboard;
  }

  onNameChange(name: string) {
  this.playerName = name;
  this.playerService.setName(name); // 🔐 Save globally
}


  toggleSettings() {
    this.showSettings = !this.showSettings;
  }

  navigateToShipsPage() {
    if (this.playerName) {
      this.router.navigate(['/place-ships']);
    }
  }

  constructor(private router: Router, private audioService: AudioService, private playerService: PlayerService) {}

  ngOnInit() {
    this.audioService.stopAll();
    this.audioService.play('titleMusic');
  }

  buttonPress() {
    this.audioService.playEffect('buttonClick');
  }
}
