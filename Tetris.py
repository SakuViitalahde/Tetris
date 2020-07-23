import pygame
from GameState import GameState
from Blocks import Blocks

WIN_WIDTH = 450
WIN_HEIGHT = 645

def main():
    running = True
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_state = GameState()
    blocks = Blocks()
    current_block = blocks.get_random_block()
    next_block = blocks.get_random_block()
    score = 0

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Current Block
        if not current_block:
            current_block = next_block

        # Next Block
        if not next_block:
            next_block = blocks.get_random_block()

        # Move Block
        if not current_block.move(game_state):
            game_state.game_state = game_state.set_current_block_to_gamestate(current_block)
            current_block = next_block
            next_block = None

        # Add Rotate, Left and Right move

        game_state.draw_window(win, current_block, score)

        # Check Tetris
        # Update Score

        if game_state.check_fail():
            pygame.quit()
            quit()
main()