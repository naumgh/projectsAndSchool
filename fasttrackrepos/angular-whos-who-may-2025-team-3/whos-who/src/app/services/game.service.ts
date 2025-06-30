import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GameService {
  //private apiUrl = "https://localhost:5001/api/games";
  private apiUrl = "http://localhost:5000/api/games";
  private gameId: string | null = null;

  constructor(private http: HttpClient) { }

  // Creates new game
  createGame(ships: any[]): Observable<any> {
    return this.http.post<any>(this.apiUrl, ships)
  }

  // Sends move/guess to the backend api (POST endpoint)
  makeMove(x: number, y: number, isPlayer = true): Observable<any> {
    if (!this.gameId) throw new Error('Game ID is not set.');
    return this.http.post<any>(`${this.apiUrl}/${this.gameId}/move`, { x, y, isPlayer });
  }

  // Gets current game state (GET endpoint)
  getGameState(): Observable<any> {
    if (!this.gameId) throw new Error('Game ID is not set.');

    return this.http.get<any>(`${this.apiUrl}/${this.gameId}`)
  }

  // Stores the Game ID
  setGameId(id: string) {
    this.gameId = id;
  }

  getGameId(): string | null {
    return this.gameId
  }

}
