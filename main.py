import sys
import pygame

from game import Game
from constants import *

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)


def main():
    game = Game(screen)
    board = game.board
    ai = game.ai

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE

                if board.is_empty_square(row, col):
                    game.make_move(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.game_mode = 'pvp'
                if event.key == pygame.K_c:
                    game.game_mode = 'pve'
                if event.key == pygame.K_r:
                    game.reset_game()
                    board = game.board
                    ai = game.ai
                

        if game.game_mode == 'pve' and game.player == 2:
            # update screen
            pygame.display.update()

            # AI move
            row, col = ai.eval(board)
            game.make_move(row, col)

        pygame.display.update()

main()