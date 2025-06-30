import { Injectable } from '@angular/core';
import { Howl, Howler } from 'howler';
import { SettingsService } from '../settings.service';

@Injectable({
  providedIn: 'root',
})
export class AudioService {
  private sounds: { [key: string]: Howl } = {};
  private soundEffects: { [key: string]: Howl } = {};

  constructor(private settingsService: SettingsService) {
    this.sounds = {
      titleMusic: new Howl({
        src: ['assets/sounds/title-page.mp3'],
        loop: true,
        volume: 0.5,
      }),
      gameMusic: new Howl({
        src: ['assets/sounds/battle-music.mp3'],
        loop: true,
        volume: 0.5,
      }),
      winMusic: new Howl({
        src: ['assets/sounds/win.mp3'],
        loop: true,
        volume: 0.5,
      }),
    };
    this.soundEffects = {
      buttonClick: new Howl({ src: ['assets/sounds/button-click.mp3'] }),
      shipPlace: new Howl({ src: ['assets/sounds/ship-placement.mp3'] }),
      miss: new Howl({ src: ['assets/sounds/miss.mp3'] }),
      hit: new Howl({ src: ['assets/sounds/hit.mp3'] }),
      startGame: new Howl({ src: ['assets/sounds/start-game.mp3'] }),
    };
  }

  play(sound: string) {
    if (this.settingsService.isSoundEnabled()) {
      this.sounds[sound]?.play();
    }
  }

  stop(sound: string) {
    this.sounds[sound]?.stop();
  }

  stopAll() {
    Object.values(this.sounds).forEach((s) => s.stop());
  }

  fadeOut(sound: string, duration = 1000) {
    this.sounds[sound]?.fade(1, 0, duration);
  }

  fadeIn(sound: string, duration = 1000) {
    this.sounds[sound]?.fade(0, 1, duration);
    this.sounds[sound]?.play();
  }

  playEffect(effect: string) {
    if (this.settingsService.isSoundEnabled()) {
      this.soundEffects[effect]?.play();
    }
  }

  setMusicVolume(volume: number) {
    Object.values(this.sounds).forEach((sound) => sound.volume(volume));
  }
}
