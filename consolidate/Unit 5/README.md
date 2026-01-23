# Unit 5: Blackjack Game - Code Commenting & Built-in Packages

A Python program demonstrating code commenting best practices and the use of Python's built-in packages for a collaborative codebase.

## What It Does

- Simulates a complete Blackjack game with player and dealer
- Tracks game statistics and saves them to JSON file
- Uses multiple built-in libraries for different functionalities
- Provides extensive comments for easy understanding and collaboration

## Requirements

- Python 3.x
- `art.py` file (contains game logo)

## How to Run

```bash
python main.py
```

The program will:
1. Load previous game statistics (if available)
2. Display menu options: play game, view stats, or quit
3. Save statistics after each game

## Built-in Libraries Used

- **random**: Generates random card values to simulate card dealing
- **json**: Saves and loads game statistics in structured format
- **datetime**: Tracks when games are played with timestamps
- **os**: Checks if files exist before reading game statistics

## Key Functions

- `deal_card()` - Returns a random card from the deck using random module
- `calculate_score(cards)` - Calculates Blackjack score with Ace conversion logic
- `compare(u_score, c_score)` - Compares scores and determines winner
- `load_stats()` - Loads game statistics from JSON file using json and os modules
- `save_stats(stats)` - Saves game statistics to JSON file using json module
- `play_game(stats)` - Main game function that runs one complete Blackjack game
- `show_stats(stats)` - Displays game statistics to the player
- `main()` - Main program entry point with game loop

## Features Demonstrated

- Extensive code commenting for collaboration
- Use of Python's built-in standard libraries
- File operations with JSON for data persistence
- Error handling with try-except blocks
- Date/time operations with datetime module
- Random number generation for game mechanics

## Files Created

- `blackjack_stats.json` - Game statistics in JSON format (wins, losses, draws, game history)

## Code Structure

The code is organized into clear sections with comments:
- Import statements with explanations
- Global variables
- Card dealing functions
- Score calculation functions
- Game comparison functions
- File operations using built-in libraries
- Main game function
- Statistics display function
- Main program entry point
