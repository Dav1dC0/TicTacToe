import os
import msvcrt


class TicTacToe:
    def __init__(self, num_players, grid_size):
        self.num_players = num_players
        self.grid_size = grid_size
        self.board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.players = []
        self.symbols = ['X', 'O', '#', '@']  # Add more symbols if needed
        self.current_player = 0
        self.winner = None

    def initialize_players(self):
        for i in range(self.num_players):
            name = input(f"Enter name for Player {i + 1}: ")
            symbol = self.symbols[i]
            self.players.append((name, symbol))
#draw board

    #check win
    #check draw
    def play(self):
        self.initialize_players()
        while not self.winner:
            self.draw_board()
            print(f"Current Player: {self.players[self.current_player][0]} ({self.players[self.current_player][1]})")
            move = input("Enter your move (row column): ")
            try:
                row, col = map(int, move.split())
                if 1 <= row <= self.grid_size and 1 <= col <= self.grid_size:
                    row -= 1
                    col -= 1
                    if self.board[row][col] == ' ':
                        self.board[row][col] = self.players[self.current_player][1]
                        if self.check_winner():
                            break
                        self.current_player = (self.current_player + 1) % self.num_players
            except ValueError:
                pass

        self.draw_board()
        if self.winner == 'Draw':
            print("It's a Draw!")
        else:
            print(f"Player {self.winner} wins!")


if __name__ == "__main__":
    num_players = int(input("Enter number of players (2 to 4): "))
    while num_players < 2 or num_players > 4:
        print("Number of players must be between 2 and 4")
        num_players = int(input("Enter number of players (2 to 4): "))

    grid_size = int(input("Enter grid size (5 to 25): "))
    while grid_size < 5 or grid_size > 25:
        print("Grid size must be between 5 and 25")
        grid_size = int(input("Enter grid size (5 to 25): "))

    game = TicTacToe(num_players, grid_size)
    game.play()
