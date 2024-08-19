import tkinter as tk
import random

# Define the game logic function
def determine_winner(user_choice):
    # List of possible choices
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    # Computer's random choice
    computer_choice = random.choice(choices)
    
    # Update the labels to display the choices
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    
    # Determine the winner based on the game rules
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Rock" and computer_choice == "Lizard") or \
         (user_choice == "Lizard" and computer_choice == "Spock") or \
         (user_choice == "Spock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Lizard") or \
         (user_choice == "Lizard" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Spock") or \
         (user_choice == "Spock" and computer_choice == "Rock") or \
         (user_choice == "Rock" and computer_choice == "Scissors"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Update the result label
    result_label.config(text=result)

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors Lizard Spock")

# Add labels to display the choices and result
user_label = tk.Label(window, text="You chose: ")
user_label.pack()

computer_label = tk.Label(window, text="Computer chose: ")
computer_label.pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Add buttons for each choice
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
for choice in choices:
    # Create a button for each choice and link it to the determine_winner function
    button = tk.Button(window, text=choice, command=lambda c=choice: determine_winner(c))
    button.pack()

# Run the main loop
window.mainloop()
"""
Rock Paper Scissors Lizard Spock Game
Description
This is a simple implementation of the Rock Paper Scissors Lizard Spock game using Python and the Tkinter library. The game allows users to play against the computer, with the computer making random choices.
How to Play
Run the game by executing the rock_paper_scissors_lizard_spock.py file.
Choose your move by clicking one of the buttons (Rock, Paper, Scissors, Lizard, or Spock).
The computer will make its random choice and display the result.
The game will display the winner (You, Computer, or Tie).
Game Rules
Rock beats Scissors and Lizard
Paper beats Rock and Spock
Scissors beats Paper and Lizard
Lizard beats Spock and Paper
Spock beats Rock and Scissors
Requirements
Python 3.x
Tkinter library (comes bundled with Python)
Author
[Your Name]
License
This game is released under the MIT License. See LICENSE.txt for details.
Note
This is a simple implementation of the game and can be improved with additional features, such as keeping track of scores or allowing multiple players.
"""