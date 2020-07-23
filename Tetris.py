import pygame
from GameState import GameState
from Blocks import Blocks

WIN_WIDTH = 700
WIN_HEIGHT = 645

key_timeout = {}
def getPressed(keys, key, timeout):
    global key_timeout

    if keys[key] == False:
        return False

    current_time = pygame.time.get_ticks()

    if key in key_timeout and key_timeout[key] > current_time:
        return False

    key_timeout[key] = current_time + timeout
    return True

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
        clock.tick(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Movement
            keys_pressed = pygame.key.get_pressed()
            if getPressed(keys_pressed, pygame.K_LEFT, 50) and not current_block.dropped:
                current_block.move_left(game_state)
            if getPressed(keys_pressed, pygame.K_RIGHT, 50)and not current_block.dropped:
                current_block.move_right(game_state)
            if getPressed(keys_pressed, pygame.K_DOWN, 50)and not current_block.dropped:
                current_block.dropped = True
            if getPressed(keys_pressed, pygame.K_UP, 50)and not current_block.dropped:
                current_block.rotate_block(game_state)
        

        # Next Block
        if not next_block:
            next_block = blocks.get_random_block()

        game_state.draw_window(win, current_block, score, next_block)

        # Move Block
        if not current_block.move_down(game_state):
            game_state.game_state = game_state.set_current_block_to_gamestate(current_block)
            current_block = next_block
            next_block = None
            score += 1

        score = game_state.check_tetris(score)

        if game_state.check_fail():
            pygame.quit()
            quit()
main()