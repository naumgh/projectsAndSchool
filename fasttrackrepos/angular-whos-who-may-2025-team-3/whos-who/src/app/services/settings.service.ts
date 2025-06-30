import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SettingsService {
  private soundEnabled = true;

  constructor() {
    const isBrowser = typeof window !== 'undefined' && typeof localStorage !== 'undefined';
    if (isBrowser) {
      const saved = localStorage.getItem('battleshipSettings');
      if (saved) {
        const parsed = JSON.parse(saved);
        this.soundEnabled = parsed.sound ?? true;
      }
    }
  }

  setSoundEnabled(enabled: boolean) {
    this.soundEnabled = enabled;
    const isBrowser = typeof window !== 'undefined' && typeof localStorage !== 'undefined';
    if (isBrowser) {
      localStorage.setItem('battleshipSettings', JSON.stringify({ sound: enabled }));
    }
  }

  isSoundEnabled(): boolean {
    return this.soundEnabled;
  }
}
