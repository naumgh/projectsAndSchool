import { Injectable } from '@angular/core';

export interface PlayerStats {
  name: string;
  wins: number;
  losses: number;
  games: number;
}

@Injectable({ providedIn: 'root' })
export class LeaderboardService {
  private storageKey = 'battleshipLeaderboard';

  getStats(): PlayerStats[] {
    return JSON.parse(localStorage.getItem(this.storageKey) || '[]');
  }

  saveStats(stats: PlayerStats[]) {
    localStorage.setItem(this.storageKey, JSON.stringify(stats));
  }

  updateStats(name: string, result: 'win' | 'loss') {
    const stats = this.getStats();
    const player = stats.find(p => p.name === name);

    if (player) {
      player.games++;
      result === 'win' ? player.wins++ : player.losses++;
    } else {
      stats.push({
        name,
        wins: result === 'win' ? 1 : 0,
        losses: result === 'loss' ? 1 : 0,
        games: 1
      });
    }

    this.saveStats(stats);
  }
}