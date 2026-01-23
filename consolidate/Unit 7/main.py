/// Guess the Number ////


import functions


def main():
    """Main program entry point for the Guess the Number game."""
    
    print("=" * 60)
    print("  GUESS THE NUMBER GAME - Loop Structure Demonstration")
    print("=" * 60)
    
    # Display examples of repetition in everyday life
    functions.display_repetition_examples()
    
    # Game configuration
    min_number = 1
    max_number = 100
    max_attempts = 7
    
    # Main program loop - allows multiple games
    while True:
        print("\n" + "=" * 60)
        print("Game Options:")
        print("1. Play Game")
        print("2. View Repetition Examples")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == "1":
            # Play the game - this function contains the main game loop
            won = functions.play_game(min_number, max_number, max_attempts)
            
            # Ask if player wants to play again
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y']:
                print("\nThanks for playing! Goodbye!")
                break
                
        elif choice == "2":
            # Display repetition examples again
            functions.display_repetition_examples()
            
        elif choice == "3":
            print("\nThanks for playing! Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

