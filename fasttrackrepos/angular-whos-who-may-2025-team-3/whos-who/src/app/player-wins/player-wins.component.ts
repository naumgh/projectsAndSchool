import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-player-wins',
  imports: [],
  templateUrl: './player-wins.component.html',
  styleUrl: './player-wins.component.css'
})
export class PlayerWinsComponent {
  constructor(private router: Router) {}

  goHome() {
    this.router.navigate(['/']);
  }
}
