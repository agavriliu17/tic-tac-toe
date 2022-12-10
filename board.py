import numpy as np
import pygame
from constants import *


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_squares = self.squares
        self.marked_squares = 0

    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_squares += 1

    def is_empty_square(self, row, col):
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_squares == 9

    def is_empty(self):
        return self.marked_squares == 0

    def get_empty_squares(self):
        empty_squares = []

        for row in range(ROWS):
            for col in range(COLS):
                if self.is_empty_square(row, col):
                    empty_squares.append((row, col))

        return empty_squares

    def final_state(self, show = False, screen = None):
        # return 0 if game is not over, 1 if X wins, 2 if O wins, 3 if tie

        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:

                if show:
                    start_pos = (col * SQUARE_SIZE + SQUARE_SIZE//2, 20)
                    end_pos = (col * SQUARE_SIZE + SQUARE_SIZE//2, HEIGHT - 20)
                    pygame.draw.line(screen, WIN_COLOR, start_pos, end_pos, LINE_WIDTH)

                # return the player number
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:

                if show:
                    start_pos = (20, row * SQUARE_SIZE + SQUARE_SIZE//2)
                    end_pos = (WIDTH - 20, row * SQUARE_SIZE + SQUARE_SIZE//2)
                    pygame.draw.line(screen, WIN_COLOR, start_pos, end_pos, LINE_WIDTH)
                
                return self.squares[row][0]

        # descending diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:

            if show:
                start_pos = (20, 20)
                end_pos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, WIN_COLOR, start_pos, end_pos, CROSS_WIDTH)

            return self.squares[0][0]

        # ascending diagonal win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:

            if show:
                start_pos = (20, HEIGHT - 20)
                end_pos = (WIDTH - 20, 20)
                pygame.draw.line(screen, WIN_COLOR, start_pos, end_pos, CROSS_WIDTH)
            
            return self.squares[2][0]

        # no win yet
        return 0