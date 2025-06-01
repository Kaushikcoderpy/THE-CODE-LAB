import random

# Initialize the board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

# Define AI move
def ai_move():
    while True:
        c = random.randint(0, 2)
        d = random.randint(0, 2)
        if board[c][d] == "":
            board[c][d] = "O"
            break

# Function to display the board
def display_board():
    for row in board:
        print("|".join([cell if cell != "" else " " for cell in row]))

# Function to check for a win
def check_win(player):
    return (board[0][0] == board[0][1] == board[0][2] == player or
            board[1][0] == board[1][1] == board[1][2] == player or
            board[2][0] == board[2][1] == board[2][2] == player or
            board[0][0] == board[1][0] == board[2][0] == player or
            board[0][1] == board[1][1] == board[2][1] == player or
            board[0][2] == board[1][2] == board[2][2] == player or
            board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player)

# Main game loop
while True:
    display_board()  # Show the board at the start of each turn
    # Get player input with error handling
    try:
        a = int(input("Enter the row (0-2): "))
        b = int(input("Enter the column (0-2): "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    # Validate the input
    if 0 <= a <= 2 and 0 <= b <= 2:
        if board[a][b] == "":
            board[a][b] = "X"
        else:
            print("Cell already occupied! Try again.")
            continue
    else:
        print("Invalid position! Please enter numbers between 0 and 2.")
        continue

    # Check for player win
    if check_win("X"):
        display_board()
        print("You won!")
        break

    # Check for tie
    if all(cell != "" for row in board for cell in row):
        display_board()
        print("It's a tie!")
        break

    # AI makes a move
    ai_move()

    # Check for AI win
    if check_win("O"):
        display_board()
        print("AI won! Better luck next time!")
        break
