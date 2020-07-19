import pygame
import os
import copy
import numpy as np

BACKGROUND_IMAGE = pygame.image.load(os.path.join("imgs","bg.png"))

class GameState():
    def __init__(self):
        self.game_state =  [[0] * 10 for i in range(22)]

    def draw_window(self, win, current_block):

        ## We need to parameters game state 
        ## From gamestart we draw corrent blocks
        ## Game state will be 22x10 list of lists
        ## Draw Current Block on game grid after checking collision

        win.blit(BACKGROUND_IMAGE, (0,0))
        self.drawGrid(win)
        self.draw_blocks(win, current_block)
        pygame.display.update()

    def drawGrid(self, win):
        """
        Draw grid for tetris game (22x10)
        """
        start = (70, -60)
        end = (370, 600)

        blockSize = 29 #Set the size of the grid block
        for x in range(start[0],end[0], 30):
            for y in range(start[1],end[1], 30):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(win, (230, 230, 230), rect, 1)
        
        # Draw outside frame
        frame_rect = pygame.Rect(start[0] - 1, start[1]- 1, 301, 661)
        pygame.draw.rect(win, (100, 100, 100), frame_rect, 1)

    def draw_blocks(self, win, current_block):
        """
        Draw Block in grid
        """
        start = (70, -60)
        end = (370, 600)
        blockSize = 29 #Set the size of the grid block
        current_game_state = self.set_current_block_to_gamestate(current_block)
        for index_x, x in enumerate(range(start[0],end[0], 30)):
            for index_y, y in enumerate(range(start[1],end[1], 30)):
                game_state_value = current_game_state[index_y][index_x]
                if game_state_value > 0:
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    if game_state_value == 1:
                        pygame.draw.rect(win, (230, 230, 0), rect, 0) ## Yellow
                    elif game_state_value == 2:
                        pygame.draw.rect(win, (230, 0, 0), rect, 0) ## Red
                    elif game_state_value == 3:
                        pygame.draw.rect(win, (0 ,230 , 0), rect, 0) ## Green
                    elif game_state_value == 4:
                        pygame.draw.rect(win, (0, 230, 230), rect, 0) ## Cyan
                    elif game_state_value == 5:
                        pygame.draw.rect(win, (230, 0, 230), rect, 0) ## Purple
                    elif game_state_value == 6:
                        pygame.draw.rect(win, (255, 125, 0), rect, 0) ## Orange
                    elif game_state_value == 7:
                        pygame.draw.rect(win, (0, 0, 230), rect, 0) ## Blue

    def set_current_block_to_gamestate(self, current_block):
        """
        Append current block in current gamestate.

        Returns:
            New gamestate with current block in it.
        """
        current_game_state = copy.deepcopy(self.game_state)
        for x, row in enumerate(current_block.block_matrix):
            for y, e in enumerate(row):
                if e != 0 and x + current_block.block_position[0] < 22:
                    current_game_state[x + current_block.block_position[0]][y + current_block.block_position[1]] = e

        return current_game_state

    def check_collision(self, block):
        " Check current block collsion to grid or other blocks"
        current = np.count_nonzero(self.set_current_block_to_gamestate(block))
        temp_block = copy.deepcopy(block)
        temp_block.block_position = (temp_block.block_position[0] + 1, temp_block.block_position[1])
        next_jump = np.count_nonzero(self.set_current_block_to_gamestate(temp_block))
        if current > next_jump:
            return True
        return False