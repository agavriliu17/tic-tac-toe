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
    score = [0, 0]

    def update_score():
        winner = int(board.final_state())
        score[winner - 1] += 1
        print("Score: X = {}, O = {}".format(score[0], score[1]))
        game.running = False

    def quit_game():
        pygame.quit()
        sys.exit()

    # Main loop
    while True:

        # Event loop
        for event in pygame.event.get():

            # Quit game
            if event.type == pygame.QUIT:
                quit_game()

            # Keyboard events
            if event.type == pygame.KEYDOWN:

                # Quit game
                if event.key == pygame.K_q:
                    quit_game()

                # Change game mode
                if event.key == pygame.K_g:
                    game.change_game_mode()

                # Change difficulty to completely random AI
                if event.key == pygame.K_0:
                    print("Changed difficulty to completely random AI")
                    ai.level = 0

                # Change difficulty to random/minimax AI
                if event.key == pygame.K_1:
                    print("Changed difficulty to random/minimax AI")
                    ai.level = 1

                # Change difficulty to minimax AI
                if event.key == pygame.K_2:
                    print("Changed difficulty to minimax AI")
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
                        update_score()


        if game.game_mode == PVE and game.player == 2 and game.running:

            # update screen
            pygame.display.update()

            # AI move
            row, col = ai.eval(board)
            game.make_move(row, col)
            
            if game.check_win():
                update_score()

        pygame.display.update()

main()