import pygame
import os

BACKGROUND_IMAGE = pygame.image.load(os.path.join("imgs","bg.png"))

class GameState():
    def __init__(self):
        self.game_state =  [[0] * 10 for i in range(22)]

    def draw_window(self, win, game_state):

        ## We need to parameters game state 
        ## From gamestart we draw corrent blocks
        ## Game state will be 22x10 list of lists
        ## Draw Current Block on game grid after checking collision

        win.blit(BACKGROUND_IMAGE, (0,0))
        self.drawGrid(win)
        self.draw_blocks(win, game_state)
        pygame.display.update()

    def drawGrid(self, win):
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

    def draw_blocks(self, win, game_state):
        start = (70, -60)
        end = (370, 600)
        blockSize = 29 #Set the size of the grid block
        for index_x, x in enumerate(range(start[0],end[0], 30)):
            for index_y, y in enumerate(range(start[1],end[1], 30)):
                game_state_value = self.game_state[index_y][index_x]
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