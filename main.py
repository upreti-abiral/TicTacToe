"""
Tic Tac Toe Game
----------------
Author: Abiral Upreti
Description: A console-based Tic Tac Toe game for two players.
"""

import os
import time


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9  # 3x3 grid represented as a list
        self.current_player = "X"

    def display_board(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n")
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---+---+---")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---+---+---")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8])
        print("\n")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in win_combos:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def reset(self):
        self.board = [" "] * 9
        self.current_player = "X"


def play_game():
    game = TicTacToe()
    while True:
        game.display_board()
        try:
            choice = int(input(f"Player {game.current_player}, enter position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("❌ Invalid position! Must be between 1 and 9.")
                time.sleep(1)
                continue
        except ValueError:
            print("❌ Invalid input! Enter a number between 1 and 9.")
            time.sleep(1)
            continue

        if not game.make_move(choice):
            print("⚠️ Position already taken! Try again.")
            time.sleep(1)
            continue

        if game.check_winner():
            game.display_board()
            print(f"🎉 Player {game.current_player} wins! 🎉")
            break

        if game.is_draw():
            game.display_board()
            print("🤝 It's a draw!")
            break

        game.switch_player()

    # Replay option
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == "y":
        game.reset()
        play_game()
    else:
        print("👋 Thanks for playing Tic Tac Toe!")


if __name__ == "__main__":
    play_game()
