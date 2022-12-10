import random
import copy

class AI:

    # level 0: random, level 1: random/minimax alternating, level 2: minimax
    def __init__(self, level = 0, player = 2):
        self.level = level
        self.player = player
        self.dumb_switch = True

    def random_move(self, board):
        empty_squares = board.get_empty_squares()
        index = random.randint(0, len(empty_squares) - 1)

        return empty_squares[index]

    def minimax(self, board, is_maximizing):

        # terminal case
        case = board.final_state()

        # case 1: X wins
        if case == 1:
            return 1, None # (score, move)
        # case 2: O wins
        if case == 2:
            return -1, None
        # case 3: tie
        elif board.is_full():
            return 0, None

        
        if is_maximizing:
            max_eval = -1000
            best_move = None
            empty_squares = board.get_empty_squares()
        
            for square in empty_squares:
                row, col = square
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = square

            return max_eval, best_move # (score, move)
        else:
            min_val = 1000
            best_move = None
            empty_squares = board.get_empty_squares()
        
            for square in empty_squares:
                row, col = square
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_val:
                    min_val = eval
                    best_move = square

            return min_val, best_move # (score, move)

    def eval(self, main_board):

        # Random AI
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.random_move(main_board)

        # Random/Minimax alternating AI
        elif self.level == 1:
            if self.dumb_switch:
                # random choice
                eval = 'random'
                move = self.random_move(main_board)
            else:
                # minimax choice
                eval, move = self.minimax(main_board, False)
            self.dumb_switch = not self.dumb_switch

        # Minimax AI
        else:
            eval, move = self.minimax(main_board, False)

        
        print(f'AI has chosen {move} with score {eval}.')
        return move # (row, col)
