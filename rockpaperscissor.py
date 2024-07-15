import random

def game():
    choices = ["rock", "paper", "scissors"]
    score_user = 0
    score_computer = 0

    while True:
        # User Input: Prompt the user to choose rock, paper, or scissors
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if user_choice == 'q':
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Computer Selection: Generate a random choice for the computer
        computer_choice = random.choice(choices)

        # Display the user's choice and the computer's choice
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        # Game Logic: Determine the winner based on the user's choice and the computer's choice
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            score_user += 1
        else:
            print("You lose!")
            score_computer += 1

        # Display the score
        print(f"Score - You: {score_user}, Computer: {score_computer}\n")

    print("Thanks for playing!")

# Call the game function
game()
