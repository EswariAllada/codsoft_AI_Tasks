import random

# Define constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Minimax scoring constants
DRAW = 0
WIN = 1
LOSS = -1

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
        self.current_player = PLAYER_X  # Player X starts
        self.game_over = False

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_win(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]):  # Row
                return True
            if all([self.board[j][i] == player for j in range(3)]):  # Column
                return True

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != EMPTY for i in range(3) for j in range(3))

    def minimax(self, board, depth, is_maximizing):
        # Check if the game is over and evaluate the board
        if self.check_win(PLAYER_X):
            return WIN
        if self.check_win(PLAYER_O):
            return LOSS
        if self.check_draw():
            return DRAW

        # Maximizing player (AI)
        if is_maximizing:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_X
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[i][j] = EMPTY
            return best
        # Minimizing player (Human)
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = PLAYER_O
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[i][j] = EMPTY
            return best

    def find_best_move(self):
        best_value = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    self.board[i][j] = PLAYER_X  # AI's move
                    move_value = self.minimax(self.board, 0, False)
                    self.board[i][j] = EMPTY

                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)

        return best_move

    def play_game(self):
        self.print_board()

        while not self.game_over:
            if self.current_player == PLAYER_X:  # AI's turn
                print("\nAI's turn (X):")
                move = self.find_best_move()
                if move:
                    self.board[move[0]][move[1]] = PLAYER_X
                self.print_board()

                if self.check_win(PLAYER_X):
                    print("\nAI wins!")
                    self.game_over = True
                elif self.check_draw():
                    print("\nIt's a draw!")
                    self.game_over = True
                else:
                    self.current_player = PLAYER_O  # Switch player

            else:  # Human's turn
                print("\nYour turn (O):")
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row (0, 1, 2): "))
                        col = int(input("Enter column (0, 1, 2): "))

                        if self.board[row][col] == EMPTY:
                            self.board[row][col] = PLAYER_O
                            valid_move = True
                        else:
                            print("This spot is already taken. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid move. Please enter row and column between 0 and 2.")

                self.print_board()

                if self.check_win(PLAYER_O):
                    print("\nYou win!")
                    self.game_over = True
                elif self.check_draw():
                    print("\nIt's a draw!")
                    self.game_over = True
                else:
                    self.current_player = PLAYER_X  # Switch player


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
#output 
 |   |  
-----
  |   |  
-----
  |   |  
-----

#AI's turn (X):
X |   |  
-----
  |   |  
-----
  |   |  
-----

#Your turn (O):
#Enter row (0, 1, 2): 1
#Enter column (0, 1, 2): 2
X |   |  
-----
  |   | O
-----
  |   |  
-----

#AI's turn (X):
X |   | X
-----
  |   | O
-----
  |   |  
-----

#Your turn (O):
#Enter row (0, 1, 2): 0
#Enter column (0, 1, 2): 1
X | O | X
-----
  |   | O
-----
  |   |  
-----

#AI's turn (X):
X | O | X
-----
  | X | O
-----
  |   |  
-----

#Your turn (O):
#Enter row (0, 1, 2): 3
#Enter column (0, 1, 2): 0
#Invalid move. Please enter row and column between 0 and 2.
#Enter row (0, 1, 2): 2
#Enter column (0, 1, 2): 0
X | O | X
-----
  | X | O
-----
O |   |  
-----

#AI's turn (X):
X | O | X
-----
  | X | O
-----
O |   | X
-----

#AI wins!
