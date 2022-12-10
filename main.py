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

        # Event loop
        for event in pygame.event.get():

            # Quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Keyboard events
            if event.type == pygame.KEYDOWN:

                # Player vs Player
                if event.key == pygame.K_p:
                    game.game_mode = 'pvp'

                # Player vs AI
                if event.key == pygame.K_c:
                    game.game_mode = 'pve'

                # Completely random AI
                if event.key == pygame.K_0:
                    ai.level = 0

                # Random AI with minimax
                if event.key == pygame.K_1:
                    ai.level = 1

                # Minimax AI
                if event.key == pygame.K_2:
                    ai.level = 2

                # Reset game
                if event.key == pygame.K_r:
                    game.reset_game()
                    board = game.board
                    ai = game.ai

            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                
                # human mark sqr
                if board.is_empty_square(row, col) and game.running:
                    game.make_move(row, col)

                    if game.check_win():
                        game.running = False


        if game.game_mode == 'pve' and game.player == 2 and game.running:

            # update screen
            pygame.display.update()

            # AI move
            row, col = ai.eval(board)
            game.make_move(row, col)
            
            if game.check_win():
                game.running = False

        pygame.display.update()

main()