import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AudioService } from '../../services/audio-service/audio.service';

type CellStatus = 'empty' | 'miss' | 'hit';

export interface Cell {
  status: CellStatus;
  row: number;
  col: number;
  hasBoat: boolean;
  boatEmoji?: string;
}

@Component({
  selector: 'app-grid',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent {
  @Input() grid: Cell[][] = [];
  @Input() showBoats: boolean = true;
  @Input() cellClickDisabled: boolean = false;
  @Output() cellClicked = new EventEmitter<Cell>();


  constructor(private audioService: AudioService){}

  handleClick(cell: Cell): void {
  this.cellClicked.emit(cell);
}

  rowLabels: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];
  colLabels: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

  onCellClick(cell: Cell): void {
    if (!this.cellClickDisabled) {
      this.cellClicked.emit(cell);
      console.log(cell);
    }
  }

  missed(){
    this.audioService.playEffect('miss');
  }

  hit(){
    this.audioService.playEffect('hit');
  }
}

