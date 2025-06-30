import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-ship',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ship.component.html',
  styleUrls: ['./ship.component.css']
})
export class ShipComponent {
  @Input() name: string = '';
  @Input() length: number = 0;
  @Input() imageUrl: string = '';
  @Input() isPlaced: boolean = false;
  @Output() selected = new EventEmitter<string>();

  onClick() {
    if (!this.isPlaced) {
      this.selected.emit(this.name);
    }
  }
}
