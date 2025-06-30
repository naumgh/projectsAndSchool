import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-computer-wins',
  imports: [],
  templateUrl: './computer-wins.component.html',
  styleUrl: './computer-wins.component.css',
  standalone: true
})
export class ComputerWinsComponent {
  constructor(private router: Router) {}

  goHome() {
    this.router.navigate(['/']);
  }

}
