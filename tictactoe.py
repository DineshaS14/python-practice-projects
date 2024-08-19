import random

# Function to display the current state of the board
def display_board(board):
    # Print the top border
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        # Print each cell in the row
        for cell in row:
            print("|   " + str(cell) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
    # Print the bottom border
    print("+-------" * 3 + "+")

# Function to handle user input and update the board
def enter_move(board):
    # Get user input
    move = int(input("Enter your move: "))
    # Check if the move is valid
    valid_move = False
    while not valid_move:
        # Check each cell on the board
        for row in range(3):
            for col in range(3):
                # If the cell matches the user's move, update the board
                if board[row][col] == move:
                    board[row][col] = 'O'
                    valid_move = True
        # If the move is not valid, ask for input again
        if not valid_move:
            move = int(input("Invalid move. Enter your move: "))

# Function to get a list of free cells on the board
def make_list_of_free_fields(board):
    free_fields = []
    # Check each cell on the board
    for row in range(3):
        for col in range(3):
            # If the cell is empty, add it to the list
            if isinstance(board[row][col], int):
                free_fields.append((row, col))
    return free_fields

# Function to check if the game has been won
def victory_for(board, sign):
    # Define the win conditions
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    # Check each win condition
    for condition in win_conditions:
        # If the condition is met, return True
        if condition.count(sign) == 3:
            return True
    # If no win condition is met, return False
    return False

# Function to handle the computer's move
def draw_move(board):
    # Get a list of free cells
    free_fields = make_list_of_free_fields(board)
    # Choose a random free cell
    move = random.choice(free_fields)
    # Update the board
    board[move[0]][move[1]] = 'X'

# Main game function
def tic_tac_toe():
    # Initialize the board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Initialize the computer's first move
    board[1][1] = 'X'
    # Display the initial board
    display_board(board)
    # Game loop
    while True:
        # Handle user input
        enter_move(board)
        # Display the updated board
        display_board(board)
        # Check if the user has won
        if victory_for(board, 'O'):
            print("You win!")
            break
        # Check if the game is a tie
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        # Handle the computer's move
        draw_move(board)
        # Display the updated board
        display_board(board)
        # Check if the computer has won
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        # Check if the game is a tie
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

# Start the game
tic_tac_toe()
"""
Tic Tac Toe Game
Description:
This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players, 'X' and 'O', to play against each other on a 3x3 grid.
How to Play:
Run the game by executing the tic_tac_toe.py file.
Player 'X' makes the first move, followed by player 'O'.
To make a move, simply type the number of the space where you want to place your piece.
The game checks for a winner after each move.
If all spaces are filled and no player has won, the game is a tie.
Features
Simple command-line interface
3x3 grid for playing
Two player support ('X' and 'O')
Automatic checking for winner or tie
Requirements
Python 3.x
Author:
Dinesha Shair
License:
This game is released under the MIT License. See LICENSE.txt for details.
Note
This is a simple implementation of Tic Tac Toe and can be improved with additional features, such as AI opponents or more advanced game logic.
"""