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
        current_block.move()

        # Check collision in move

        game_state.draw_window(win, current_block)

        # Check tetris
        # Update Score

main()