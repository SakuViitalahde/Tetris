import pygame
from GameState import GameState

WIN_WIDTH = 450
WIN_HEIGHT = 645

def main():
    running = True
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_state = GameState()

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Current Block
        # Next Block
        # Move Block
        # Check collision in move

        game_state.draw_window(win, game_state)

        # Check tetris
        # Update Score

main()