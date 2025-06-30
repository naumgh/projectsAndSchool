import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-input-field',
  templateUrl: './input-field.component.html',
  styleUrls: ['./input-field.component.css'],
  imports:[FormsModule],
  standalone: true
})
export class InputFieldComponent implements OnInit{
  
  constructor() {}

  ngOnInit(): void {}

  name: string = '';

  setName(name: string) {
    this.name = name;
    this.nameChange.emit(this.name);
  }

  @Output() nameChange: EventEmitter<string> = new EventEmitter<string>();
}