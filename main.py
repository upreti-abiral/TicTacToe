board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner():
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        a = position[0]
        b = position[1]
        c = position[2]

        if board[a] == board[b] == board[c]:
            return True

    return False

def check_draw():
    for position in board:
        if position not in ["X", "O"]:
            return False

    return True

player = "X"

while True:
    display_board()

    while True:
        try:
            choice = int(input("Player " + player + ", choose a position (1-9): "))

            if choice < 1 or choice > 9:
                print("Please enter a number from 1 to 9.")
            elif board[choice - 1] in ["X", "O"]:
                print("That position is already taken.")
            else:
                board[choice - 1] = player
                break

        except ValueError:
            print("Please enter a number.")

    if check_winner():
        display_board()
        print("Player " + player + " wins!")
        break

    if check_draw():
        display_board()
        print("It's a draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
