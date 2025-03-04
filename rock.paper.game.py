import random

# Choices available
choices = ["rock", "paper", "scissors"]

# Score tracking
user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    
    computer_score += 1
    return "You lose!"

while True:
    # User Input
    user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
    
    if user_choice == "exit":
        print(f"\nFinal Score: You {user_score} - {computer_score} Computer")
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine and display result
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print(f"Score: You {user_score} - {computer_score} Computer\n")
