import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avail_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        vaild_square = False
        val = None
        while not vaild_square:
            square = int(input(self.letter + '\'s turn. Choice from 0-9: '))
            try:
                val = int(square)
                if val not in game.avail_moves():
                    raise ValueError
                vaild_square = True
            except ValueError:
                print("Invalid Moves, Try Again.")

class sharpGame:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[_ * 3: (_ + 1) * 3] for _ in range(3)]:
            print(" | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print(" | " + " | ".join(row) + " | ")

    def avail_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves
    
    def empty_square(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(square, letter):
        row_ind = square
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diag_one = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag_one]):
                return True

            diag_two = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag_two]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"
    while game.empty_square():
        if letter == "0":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" Makes a move to the square {square}")
                game.print_board()
                print(" ")
            
            if game.current_winner:
                if print_game:
                    print(letter + " Wins")
                    return letter

            letter = "O" if letter == "X" else "X"
    if print_game:
        print("It\'s a tie")

if __name__ == "__main__":      
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = sharpGame()
    play(t, x_player, o_player, print_game=True)
