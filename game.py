import pygame

from ai import AI
from board import Board
from constants import *

class Game:
    def __init__(self, screen, difficulty = 0, game_mode = PVP):
        self.screen = screen
        self.board = Board()
        self.ai = AI(difficulty)
        self.player = 1
        self.show_lines()
        self.game_mode = game_mode
        self.running = True

    def show_lines(self):
        self.screen.fill(BG_COLOR)

        # Vertical lines
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def draw_fig(self, row, col):
        if self.player == 1:
            # Draw X
            start_desc = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            end_desc = ((col + 1) * SQUARE_SIZE - OFFSET, (row + 1) * SQUARE_SIZE - OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            start_asc = ((col + 1) * SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)
            end_asc = (col * SQUARE_SIZE + OFFSET, (row + 1) * SQUARE_SIZE - OFFSET)
            pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player == 2:
            # Draw O
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(self.screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)


    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def reset_game(self):
        self.__init__(self.screen, self.ai.level, self.game_mode)

    def check_win(self):
        return self.board.final_state(show=True, screen=self.screen) != 0 or self.board.is_full()

    def change_game_mode(self):
        self.game_mode = PVP if self.game_mode == PVE else PVE
