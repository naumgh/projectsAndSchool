import { Component, Input } from '@angular/core';
import { LeaderboardService, PlayerStats } from '../services/leaderboard.service';
import { NgIf, NgFor } from '@angular/common';

@Component({
  selector: 'app-leaderboard',
  standalone: true,
  imports: [NgIf, NgFor],
  templateUrl: './leaderboard.component.html',
  styleUrl: './leaderboard.component.css'
})
export class LeaderboardComponent {
  @Input() close!: () => void;

  players: PlayerStats[] = [];

  constructor(private leaderboardService: LeaderboardService) {}

  ngOnInit() {
    this.players = this.leaderboardService
      .getStats()
      .sort((a, b) => b.games - a.games);
  }
}