import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./title-screen/title-screen.component').then(m => m.TitleScreenComponent)
  },
  {
    path: 'home',
    redirectTo: '',
    pathMatch: 'full'
  },
  {
    path: 'place-ships',
    loadComponent: () =>
      import('./ship-placement/ship-placement.component').then(m => m.ShipPlacementComponent)
  },
  {
    path: 'game',
    loadComponent: () =>
      import('./game-screen/game-screen.component').then(m => m.GameScreenComponent)
  },
  {
    path: 'settings',
    loadComponent: () =>
      import('./Components/settings/settings.component').then(m => m.SettingsComponent)
  },
  {
    path: 'player-wins',
    loadComponent: () =>
      import('./player-wins/player-wins.component').then(m => m.PlayerWinsComponent)
  },
  {
    path: 'computer-wins',
    loadComponent: () =>
      import('./computer-wins/computer-wins.component').then(m => m.ComputerWinsComponent)
  }
];

export class AppRoutingModule {}