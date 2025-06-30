import { Injectable } from '@angular/core';

interface Coordinate {
  x: number;
  y: number;
}

@Injectable({
  providedIn: 'root'
})
export class AiService {
  private availableMoves: Coordinate[] = [];
  private targetQueue: Coordinate[] = [];
  private currentTarget: Coordinate[] = [];

  constructor() {
    this.reset();
  }

  reset() {
    this.availableMoves = [];
    this.targetQueue = [];
    this.currentTarget = [];

    for (let x = 0; x < 10; x++) {
      for (let y = 0; y < 10; y++) {
        this.availableMoves.push({ x, y });
      }
    }

    this.shuffle(this.availableMoves);
  }

  markHit(x: number, y: number) {
    this.currentTarget.push({ x, y });
    if (this.isInAvailable(x, y)) {
      this.removeFromAvailable(x, y);
    }
  }

queueAdjacentTargets(x: number, y: number) {
  const directions = [
    { x: -1, y: 0 },
    { x: 1, y: 0 },
    { x: 0, y: -1 },
    { x: 0, y: 1 }
  ];

  for (const dir of directions) {
    const nx = x + dir.x;
    const ny = y + dir.y;

    if (this.isValid(nx, ny)) {
      this.targetQueue.push({ x: nx, y: ny }); // only add — don't remove yet
    }
  }
}

  registeredSunk() {
    this.targetQueue = [];
    this.currentTarget = [];
  }

 getNextMove(): Coordinate {
  let move;
  if (this.targetQueue.length > 0) {
    move = this.targetQueue.shift()!;
  } else {
    move = this.availableMoves.pop()!;
  }

  this.removeFromAvailable(move.x, move.y);
  return move;
}

  private isValid(x: number, y: number): boolean {
    return (
      x >= 0 &&
      x < 10 &&
      y >= 0 &&
      y < 10 &&
      !this.targetQueue.some(m => m.x === x && m.y === y) &&
      this.availableMoves.some(m => m.x === x && m.y === y)
    );
  }

  private isInAvailable(x: number, y: number): boolean {
  return this.availableMoves.some(m => m.x === x && m.y === y);
}

  private removeFromAvailable(x: number, y: number) {
  const index = this.availableMoves.findIndex(m => m.x === x && m.y === y);
  if (index !== -1) {
    this.availableMoves.splice(index, 1);
  }
}

  private shuffle(array: Coordinate[]) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }
}