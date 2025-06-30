import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';
import { GridComponent, Cell } from '../Components/grid/grid.component';
import { GameStateService } from '../services/game-state-service/game-state.service';
import { GameService } from '../services/game.service';
import { SettingsComponent } from '../Components/settings/settings.component';
import { BattleshipHeaderComponent } from '../Components/battleship-header/battleship-header.component';
import { NewQuitModComponent } from '../Components/new-quit-mod/new-quit-mod.component';
import { AudioService } from '../services/audio-service/audio.service';

type CellStatus = 'empty' | 'miss' | 'hit';

interface ShipState {
  name: string;
  emoji?: string;
  length: number;
  imageUrl: string;
  partsLeft: number;
  isPlaced: boolean;
  coordinates?: { row: number; col: number }[];
}

@Component({
  selector: 'app-ship-placement',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    GridComponent,
    SettingsComponent,
    BattleshipHeaderComponent,
    NewQuitModComponent,
  ],
  templateUrl: './ship-placement.component.html',
  styleUrls: ['./ship-placement.component.css'],
})
export class ShipPlacementComponent {
  ships: ShipState[] = [
    {
      name: 'Carrier',
      length: 5,
      imageUrl: 'assets/images/carrier.png',
      emoji: '🛳️',
      partsLeft: 5,
      isPlaced: false,
    },
    {
      name: 'Battleship',
      length: 4,
      imageUrl: 'assets/images/battleship_top.png',
      emoji: '🚢',
      partsLeft: 4,
      isPlaced: false,
    },
    {
      name: 'Submarine',
      length: 3,
      imageUrl: 'assets/images/submarine2.png',
      emoji: '🐋',
      partsLeft: 3,
      isPlaced: false,
    },
    {
      name: 'Cruiser',
      length: 3,
      imageUrl: 'assets/images/cruiser.png',
      emoji: '🛥️',
      partsLeft: 3,
      isPlaced: false,
    },
    {
      name: 'Destroyer',
      length: 2,
      imageUrl: 'assets/images/destroyer.png',
      emoji: '🚤',
      partsLeft: 2,
      isPlaced: false,
    },
  ];

  showSettings: boolean = false;

  selectedShip: ShipState | null = null;
  orientation: 'horizontal' | 'vertical' = 'horizontal';

  grid: Cell[][] = [];

  constructor(
    private router: Router, 
    private gameState: GameStateService,
    private gameService: GameService,
	private audioService: AudioService
  ) {
    this.initializeGrid();
  }

  initializeGrid() {
    this.grid = Array.from({ length: 10 }, (_, row) =>
      Array.from({ length: 10 }, (_, col) => ({
        status: 'empty',
        row,
        col,
        hasBoat: false,
        boatEmoji: '',
      }))
    );
  }

  toggleOrientation() {
    this.orientation =
      this.orientation === 'horizontal' ? 'vertical' : 'horizontal';
  }

  onShipSelected(name: string) {
    this.selectedShip =
      this.ships.find((s) => s.name === name && !s.isPlaced) || null;
    console.log(name);
  }

  onCellClick(cell: Cell) {
    if (!this.selectedShip || this.selectedShip.partsLeft <= 0) return;

    const startRow = cell.row;
    const startCol = cell.col;

    for (let i = 0; i < this.selectedShip.length; i++) {
      const r = this.orientation === 'vertical' ? startRow + i : startRow;
      const c = this.orientation === 'horizontal' ? startCol + i : startCol;

      if (!this.grid[r]?.[c] || this.grid[r][c].hasBoat) return;
    }

    const placedCoords: { row: number; col: number }[] = [];
    for (let i = 0; i < this.selectedShip.length; i++) {
      const r = this.orientation === 'vertical' ? startRow + i : startRow;
      const c = this.orientation === 'horizontal' ? startCol + i : startCol;
      this.grid[r][c].hasBoat = true;
      this.grid[r][c].boatEmoji = this.selectedShip.emoji;
      placedCoords.push({ row: r, col: c });
    }

    this.audioService.playEffect('shipPlace');
    this.selectedShip.isPlaced = true;
    this.selectedShip.partsLeft = 0;
    this.selectedShip.coordinates = placedCoords;
    this.selectedShip = null;
  }

  undoPlacement(ship: ShipState) {
    if (!ship.coordinates) return;

    for (const coord of ship.coordinates) {
      this.grid[coord.row][coord.col].hasBoat = false;
      this.grid[coord.row][coord.col].boatEmoji = '';
    }

    ship.isPlaced = false;
    ship.partsLeft = ship.length;
    ship.coordinates = [];
  }

  allShipsPlaced(): boolean {
    return this.ships.every((ship) => ship.isPlaced);
  }

  startGame() {
    if (!this.allShipsPlaced()) return;
    
    const transformedShips = this.ships.map(ship => ({
      name: ship.name,
      length: ship.length,
      positions: ship.coordinates?.map(coord => ({
        x: coord.col,
        y: coord.row
      })) || []
    }))
    
    this.gameService.createGame(transformedShips).subscribe({
      next: (response) => {
        console.log('Game created:', response)
        this.gameService.setGameId(response.id)
        this.gameState.setPlayerGrid(this.grid)
        this.router.navigate(['/game'])
		this.audioService.stopAll();
		this.audioService.playEffect('startGame');
		this.audioService.play('gameMusic');
      },
      error: (err) => {
        console.error('Failed to create game:', err)
      }
    })

  }

  toggleSettings() {
    this.showSettings = !this.showSettings;
  }

  buttonPress() {
    this.audioService.playEffect('buttonClick');
  }
}
