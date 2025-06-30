import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class PlayerService {
  private playerName: string = '';

  setName(name: string) {
    this.playerName = name;
  }

  getName(): string {
    return this.playerName;
  }
}