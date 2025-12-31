import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """Prompts the user for their choice and validates the input."""
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the round.
    Returns: 
        'user' if user wins, 
        'computer' if computer wins, 
        'tie' if it's a tie.
    """
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """Displays the choices and the result of the round."""
    print(f"\nYou chose: **{user_choice.capitalize()}**")
    print(f"Computer chose: **{computer_choice.capitalize()}**")

    if winner == 'user':
        print("**You win!** 🎉")
    elif winner == 'computer':
        print("**Computer wins!** 🤖")
    else:
        print("**It's a tie!** 🤝")

def play_game():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("--- Welcome to Rock-Paper-Scissors! ---")
    #     
    while True:
        print("\n--- New Round ---")
        
        # User Input & Computer Selection
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Game Logic
        winner = determine_winner(user_choice, computer_choice)

        # Display Result
        display_result(user_choice, computer_choice, winner)

        # Score Tracking (Optional)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"**Current Score:** You: {user_score} | Computer: {computer_score}")

        # Play Again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\n--- Final Score ---")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()