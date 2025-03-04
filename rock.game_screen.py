import random
import tkinter as tk
from tkinter import messagebox

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    lbl_computer_choice.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    lbl_result.config(text=result)
    lbl_score.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to exit the game
def exit_game():
    root.destroy()

# Initialize scores
user_score = 0
computer_score = 0

# Create GUI Window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12)).pack(pady=10)

# Buttons for user choice
btn_rock = tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: determine_winner("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: determine_winner("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: determine_winner("Scissors"))
btn_scissors.pack(pady=5)

# Labels to display choices and results
lbl_computer_choice = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
lbl_computer_choice.pack(pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
lbl_result.pack(pady=5)

lbl_score = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12))
lbl_score.pack(pady=10)

# Exit Button
btn_exit = tk.Button(root, text="Exit Game", font=("Arial", 12), command=exit_game)
btn_exit.pack(pady=10)

# Run the application
root.mainloop()
