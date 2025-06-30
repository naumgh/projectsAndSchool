import { NgIf } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AudioService } from '../../services/audio-service/audio.service';

@Component({
  selector: 'app-confirm-screen',
  imports: [RouterLink, NgIf],
  templateUrl: './confirm-screen.component.html',
  styleUrl: './confirm-screen.component.css',
})
export class ConfirmScreenComponent {
  @Input() choice = '';
  @Input() choiceText = '';
  @Output() close = new EventEmitter<void>();

  constructor(private audioService: AudioService){}

  buttonPress(){
    this.audioService.playEffect('buttonClick');
  }
}
