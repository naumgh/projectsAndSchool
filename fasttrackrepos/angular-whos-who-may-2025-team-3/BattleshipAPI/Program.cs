using System;
using System.Collections.Generic;

var builder = WebApplication.CreateBuilder(args);

// CORS for local Angular app
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseCors("AllowAll");

// In-memory game storage
var games = new Dictionary<Guid, GameState>();

// POST /api/games - start new game
app.MapPost("/api/games", (List<Ship> playerShips) =>
{
    var gameId = Guid.NewGuid();

    var computerShips = new List<Ship>
    {
        new Ship("Destroyer", 2, new List<Coordinate> { new(0, 0), new(0, 1) }),
        new Ship("Cruiser", 3, new List<Coordinate> { new(1, 0), new(1, 1), new(1, 2) }),
        new Ship("Submarine", 3, new List<Coordinate> { new(2, 0), new(2, 1), new(2, 2) }),
        new Ship("Battleship", 4, new List<Coordinate> { new(3, 0), new(3, 1), new(3, 2), new(3, 3) }),
        new Ship("Carrier", 5, new List<Coordinate> { new(4, 0), new(4, 1), new(4, 2), new(4, 3), new(4, 4) }),
    };

    var game = new GameState(gameId, playerShips, computerShips);
    games[gameId] = game;
    return Results.Ok(game);
});

// POST /api/games/{id}/move - make a move (player or AI)
app.MapPost("/api/games/{id:guid}/move", (Guid id, Move move) =>
{
    if (!games.TryGetValue(id, out var game))
        return Results.NotFound("Game not found.");

    if (move.IsPlayer)
    {
        // Prevent repeated player moves
        if (game.PlayerMoves.Exists(m => m.X == move.X && m.Y == move.Y))
            return Results.BadRequest("Move already made at this coordinate.");

        game.PlayerMoves.Add(move);

        var hitShip = game.ComputerShips.FirstOrDefault(ship =>
            ship.Positions.Any(pos => pos.X == move.X && pos.Y == move.Y));

        if (hitShip != null)
        {
            var hitCoord = new Coordinate(move.X, move.Y);
            game.ComputerShipHits.Add(hitCoord);

            bool isSunk = hitShip.Positions.All(pos =>
                game.ComputerShipHits.Any(hit => hit.X == pos.X && hit.Y == pos.Y));

            bool isGameOver = game.ComputerShips.All(ship =>
                ship.Positions.All(pos =>
                    game.ComputerShipHits.Any(hit => hit.X == pos.X && hit.Y == pos.Y)));

            return Results.Ok(new
            {
                result = isSunk ? "sunk" : "hit",
                move,
                hitShip = hitShip.Name,
                isSunk,
                isGameOver,
                winner = isGameOver ? "Player" : null
            });
        }

        return Results.Ok(new
        {
            result = "miss",
            move,
            hitShip = (string?)null,
            isSunk = false,
            isGameOver = false,
            winner = (string?)null
        });
    }
    else // AI Move
    {
        // Prevent repeated AI moves
        if (game.ComputerMoves.Exists(m => m.X == move.X && m.Y == move.Y))
            return Results.BadRequest("AI move already made at this coordinate.");

        game.ComputerMoves.Add(move);

        var hitShip = game.PlayerShips.FirstOrDefault(ship =>
            ship.Positions.Any(pos => pos.X == move.X && pos.Y == move.Y));

        if (hitShip != null)
        {
            var hitCoord = new Coordinate(move.X, move.Y);
            game.PlayerShipHits.Add(hitCoord);

            bool isSunk = hitShip.Positions.All(pos =>
                game.PlayerShipHits.Any(hit => hit.X == pos.X && hit.Y == pos.Y));

            bool isGameOver = game.PlayerShips.All(ship =>
                ship.Positions.All(pos =>
                    game.PlayerShipHits.Any(hit => hit.X == pos.X && hit.Y == pos.Y)));

            return Results.Ok(new
            {
                result = isSunk ? "sunk" : "hit",
                move,
                hitShip = hitShip.Name,
                isSunk,
                isGameOver,
                winner = isGameOver ? "Computer" : null
            });
        }

        return Results.Ok(new
        {
            result = "miss",
            move,
            hitShip = (string?)null,
            isSunk = false,
            isGameOver = false,
            winner = (string?)null
        });
    }
});

// GET /api/games/{id} - fetch game state
app.MapGet("/api/games/{id:guid}", (Guid id) =>
{
    if (games.TryGetValue(id, out var game))
        return Results.Ok(game);
    return Results.NotFound();
});

app.Run();

// --- Models ---
public record Coordinate(int X, int Y);
public record Ship(string Name, int Length, List<Coordinate> Positions);
public class Move
{
    public int X { get; set; }
    public int Y { get; set; }
    public bool IsPlayer { get; set; }
}
public class GameState
{
    public Guid Id { get; set; }
    public List<Ship> PlayerShips { get; set; }
    public List<Ship> ComputerShips { get; set; }
    public List<Move> PlayerMoves { get; set; } = new();
    public List<Move> ComputerMoves { get; set; } = new();
    public List<Coordinate> ComputerShipHits { get; set; } = new();
    public List<Coordinate> PlayerShipHits { get; set; } = new();

    public GameState(Guid id, List<Ship> playerShips, List<Ship> computerShips)
    {
        Id = id;
        PlayerShips = playerShips;
        ComputerShips = computerShips;
    }
}
