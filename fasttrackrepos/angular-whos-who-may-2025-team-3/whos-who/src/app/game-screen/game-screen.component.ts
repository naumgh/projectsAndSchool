import { Component, OnInit } from '@angular/core';
import { BattleshipHeaderComponent } from '../Components/battleship-header/battleship-header.component';
import { GridComponent, Cell } from '../Components/grid/grid.component';
import { GameStateService } from '../services/game-state-service/game-state.service';
import { SettingsComponent } from '../Components/settings/settings.component';
import { NgIf } from '@angular/common';
import { NewQuitModComponent } from '../Components/new-quit-mod/new-quit-mod.component';
import { AudioService } from '../services/audio-service/audio.service';
import { GameService } from '../services/game.service';
import { AiService } from '../services/ai.service';
import { Router, RouterModule } from '@angular/router';
import { LeaderboardComponent } from '../leaderboard/leaderboard.component';
import { LeaderboardService } from '../services/leaderboard.service';
import { PlayerService } from '../services/player.service';

@Component({
  selector: 'app-game-screen',
  standalone: true,
  imports: [
    NgIf,
    BattleshipHeaderComponent,
    GridComponent,
    SettingsComponent,
    NewQuitModComponent,
    RouterModule,
    LeaderboardComponent,
  ],
  templateUrl: './game-screen.component.html',
  styleUrls: ['./game-screen.component.css'],
})
export class GameScreenComponent implements OnInit {
  playerGrid: Cell[][] = [];
  opponentGrid: Cell[][] = [];
  isMoveInProgress = false;
  showSettings = false;
  isPlayerTurn = true;
  usedMoves: Set<string> = new Set();

  constructor(
    private gameState: GameStateService,
    private gameService: GameService,
    private audioService: AudioService,
    private aiService: AiService,
    private router: Router,
    private leaderboardService: LeaderboardService,
    private playerService: PlayerService
  ) {}

  ngOnInit(): void {
    this.playerGrid = this.gameState.getPlayerGrid();

    this.opponentGrid = Array.from({ length: 10 }, (_, row) =>
      Array.from({ length: 10 }, (_, col) => ({
        status: 'empty',
        row,
        col,
        hasBoat: false,
        boatEmoji: '',
      }))
    );
  }

  onOpponentCellClick(cell: Cell) {
    if (!this.isPlayerTurn || this.isMoveInProgress || cell.status !== 'empty') return;

    this.isMoveInProgress = true;
    console.log('Player clicked:', cell);

    this.gameService.makeMove(cell.col, cell.row, true).subscribe({
      next: (response) => {
        console.log('Move response:', response);

        if (response.result === 'hit' || response.result === 'sunk') {
          this.audioService.playEffect('hit');
          cell.status = 'hit';
          cell.boatEmoji = '🔥';
        } else {
          this.audioService.playEffect('miss');
          cell.status = 'miss';
        }

        console.log(`[PLAYER MOVE] Marked (${cell.row}, ${cell.col}) as ${cell.status}`);

        if (response.isGameOver) {
          this.audioService.stopAll();
          this.audioService.play('winMusic');
          alert(`Game Over! You won!`);
          const playerName = this.playerService.getName();
          if (playerName) {
            this.leaderboardService.updateStats(playerName, 'win');
          }
          this.router.navigate(['/']);
          return;
        }

        this.isPlayerTurn = false;
        setTimeout(() => this.performComputerMove(), 700);
      },
      error: (err) => {
        console.error('Error making move:', err);
        alert('There was an error making your move. Please try again.');
      },
      complete: () => {
        this.isMoveInProgress = false;
      },
    });
  }

  performComputerMove() {
    console.log('AI move queue:', this.aiService['targetQueue']);
    console.log('AI available moves:', this.aiService['availableMoves']);

    const move = this.aiService.getNextMove();
    if (!move) {
      console.log('AI has no valid moves left');
      return;
    }

    const { x, y } = move;
    const moveKey = `${x},${y}`;

    if (this.usedMoves.has(moveKey)) {
      console.warn('AI tried duplicate move, retrying:', moveKey);
      setTimeout(() => this.performComputerMove(), 100);
      return;
    }

    this.usedMoves.add(moveKey);

    const cell = this.playerGrid[y][x];
    if (cell.status !== 'empty') {
      console.warn('Cell not empty but move not tracked? Skipping:', x, y);
      return;
    }

    this.gameService.makeMove(x, y, false).subscribe({
      next: (response) => {
        cell.status = response.result === 'hit' || response.result === 'sunk' ? 'hit' : 'miss';

        if (response.result === 'hit' || response.result === 'sunk') {
          this.audioService.playEffect('hit');
          this.aiService.markHit(x, y);
        } else {
          this.audioService.playEffect('miss');
        }

        if (response.result === 'sunk') {
          this.aiService.registeredSunk();
          console.log(`AI sunk your ${response.hitShip}`);
        } else if (response.result === 'hit') {
          this.aiService.queueAdjacentTargets(x, y);
        }

        if (response.isGameOver) {
          console.log('Game over response:', response);
          alert(`Game Over! Computer won!`);
          const playerName = this.playerService.getName();
          if (playerName) {
            this.leaderboardService.updateStats(playerName, 'loss');
          }
          this.router.navigate(['/']);
          return;
        }

        this.isPlayerTurn = true;
      },
      error: (err) => {
        console.error('AI move error:', err);
      }
    });
  }

  toggleSettings() {
    this.showSettings = !this.showSettings;
  }

  buttonPress() {
    this.audioService.playEffect('buttonClick');
  }
}
