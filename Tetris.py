import pygame
import os

WIN_WIDTH = 450
WIN_HEIGHT = 645
BACKGROUND_IMAGE = pygame.image.load(os.path.join("imgs","bg.png"))


def draw_window(win, game_state):

    ## We need to parameters game state 
    ## From gamestart we draw corrent blocks
    ## Game state will be 22x10 list of lists

    ## Current Block could be in different game_state like grid

    win.blit(BACKGROUND_IMAGE, (0,0))
    drawGrid(win)
    draw_blocks(win, game_state)
    pygame.display.update()

def drawGrid(win):
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

def draw_blocks(win, game_state):
    # 0 - 9 column indexes
    # 0 - 21 row indexes
    game_state[3][3] = 3
    game_state[3][4] = 3
    game_state[3][5] = 3  
    game_state[3][6] = 3   

    game_state[14][8] = 5
    game_state[15][8] = 5
    game_state[16][8] = 5
    game_state[17][8] = 5

    game_state[21][0] = 1
    game_state[21][1] = 1
    game_state[21][2] = 1
    game_state[21][3] = 1

    start = (70, -60)
    end = (370, 600)
    blockSize = 29 #Set the size of the grid block
    for index_x, x in enumerate(range(start[0],end[0], 30)):
        for index_y, y in enumerate(range(start[1],end[1], 30)):
            game_state_value = game_state[index_y][index_x]
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



def main():
    running = True
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_state = [[0] * 10 for i in range(22)]
    print(len(game_state))
    print(len(game_state[0]))


    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw_window(win, game_state)

main()