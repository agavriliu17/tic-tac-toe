import random

class AI:

    def __init__(self, level, player=2):
        self.level = level
        self.player = player

    def random_move(self, board):
        empty_squares = board.get_empty_squares()
        index = random.randint(0, len(empty_squares) - 1)

        return empty_squares[index]

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            move = self.random_move(main_board)
        else:
            # minimax choice
            pass

        return move # (row, col)
