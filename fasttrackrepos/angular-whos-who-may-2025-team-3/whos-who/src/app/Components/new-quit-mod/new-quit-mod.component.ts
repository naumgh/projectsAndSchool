import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ConfirmScreenComponent } from '../confirm-screen/confirm-screen.component';
import { NgIf } from '@angular/common';
import { AudioService } from '../../services/audio-service/audio.service';

@Component({
  selector: 'app-new-quit-mod',
  imports: [FormsModule, ConfirmScreenComponent, NgIf],
  templateUrl: './new-quit-mod.component.html',
  styleUrl: './new-quit-mod.component.css'
})
export class NewQuitModComponent {
  choice = '';
  choiceText = '';
  showConfirm = false;

  constructor(private audioService: AudioService){}

  buttonPress(){
    this.audioService.playEffect('buttonClick');
  }

  newGame() {
    this.choice = 'start a new game';
    this.choiceText = 'Your current progress will not be saved. You will return to the ship placement screen.';
    this.showConfirm = true;
  }

  quit() {
    this.choice = 'quit';
    this.choiceText = 'Your current progress will not be saved.';
    this.showConfirm = true;
  }

  onCloseConfirm() {
    this.showConfirm = false;
  }
}
