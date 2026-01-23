"""Blackjack Game Project"""

import random
import json
import datetime
import os
from art import logo

STATS_FILE = "blackjack_stats.json"


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculate score from cards. Returns 0 for Blackjack, converts Ace if bust."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compare user and computer scores to determine winner."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def load_stats():
    """Load game statistics from JSON file."""
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, 'r') as file:
                stats = json.load(file)
                print(f"✓ Loaded previous statistics: {stats['games_played']} games played")
                return stats
        except:
            print("⚠ Could not load stats file. Starting fresh.")
            return {"games_played": 0, "wins": 0, "losses": 0, "draws": 0, "games": []}
    else:
        print("ℹ No previous statistics found. Starting new game history.")
        return {"games_played": 0, "wins": 0, "losses": 0, "draws": 0, "games": []}


def save_stats(stats):
    """Save game statistics to JSON file using json module."""
    try:
        with open(STATS_FILE, 'w') as file:
            json.dump(stats, file, indent=4)
    except:
        print("⚠ Could not save statistics to file.")


def play_game(stats):
    """Run one complete game of Blackjack and return updated stats."""
    print(logo)
    
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer must hit until score reaches 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    game_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Game ended at: {game_time}")
    
    result = compare(user_score, computer_score)
    print(result)
    
    stats["games_played"] += 1
    
    game_record = {
        "timestamp": game_time,
        "user_score": user_score,
        "computer_score": computer_score,
        "result": result
    }
    stats["games"].append(game_record)
    
    if "win" in result.lower() and "lose" not in result.lower():
        stats["wins"] += 1
    elif "lose" in result.lower():
        stats["losses"] += 1
    else:
        stats["draws"] += 1
    
    return stats


def show_stats(stats):
    """Display game statistics to the player."""
    print("\n" + "="*60)
    print("📊 GAME STATISTICS")
    print("="*60)
    print(f"Total Games Played: {stats['games_played']}")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Draws: {stats['draws']}")
    
    if stats['games_played'] > 0:
        win_percentage = (stats['wins'] / stats['games_played']) * 100
        print(f"Win Percentage: {win_percentage:.1f}%")
    
    print("="*60 + "\n")


def main():
    """Main program entry point."""
    stats = load_stats()
    
    while True:
        choice = input("Do you want to play a game of Blackjack? Type 'y' to play, 's' for stats, 'n' to quit: ").lower()
        
        if choice == "y":
            print("\n" * 20)
            stats = play_game(stats)
            save_stats(stats)
        elif choice == "s":
            show_stats(stats)
        elif choice == "n":
            print("\n👋 Thanks for playing! Your statistics have been saved.")
            print(f"📊 Final Stats: {stats['wins']} wins, {stats['losses']} losses, {stats['draws']} draws")
            break
        else:
            print("⚠ Invalid choice. Please type 'y', 's', or 'n'.")


if __name__ == "__main__":
    main()

