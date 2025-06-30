import { Injectable } from '@angular/core';
import { Cell } from '../../Components/grid/grid.component';

@Injectable({
  providedIn: 'root'
})
export class GameStateService {

  constructor() { }

  playerGrid: Cell[][] = [];
  opponentGrid: Cell[][] = [];

  setPlayerGrid(grid: Cell[][]) {
    this.playerGrid = grid;
  }

  getPlayerGrid(): Cell[][] {
    return this.playerGrid;
  }

  setOpponentGrid(grid: Cell[][]) {
    this.opponentGrid = grid;
  }

  getOpponentGrid(): Cell[][] {
    return this.opponentGrid;
  }

}
