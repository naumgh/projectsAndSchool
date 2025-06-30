import { Component, Output, EventEmitter, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AudioService } from '../../services/audio-service/audio.service';
import { SettingsService } from '../../services/settings.service';

@Component({
  selector: 'app-settings',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './settings.component.html',
  styleUrl: './settings.component.css',
})
export class SettingsComponent {
  @Output() close = new EventEmitter<void>();
  sound =true;

  constructor(private audioService: AudioService, private settingsService: SettingsService) {
    this.sound = this.settingsService.isSoundEnabled();
  }

  toggleSound() {
    this.settingsService.setSoundEnabled(this.sound);
  }


  buttonPress() {
    this.audioService.playEffect('buttonClick');
  }

  settings = {
    sound: true,
    difficulty: 'medium',
  };

  ngOnInit() {
    const saved = localStorage.getItem('gameSettings');
    if (saved) {
      this.settings = JSON.parse(saved);
    }
  }

  saveSettings() {
    localStorage.setItem('gameSettings', JSON.stringify(this.settings));
    this.close.emit();
  }
}
