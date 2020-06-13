import numpy as np

class Block():
    def __init__(self):
        super().__init__()
        self.block_position = (3,5)
        self.block_matrix = [] # This is 2x2,3x3 or 4x4 depending from blocktype
    
    def rotate_block(self):
        """
        Rotate Matrix 90 degrees clockwise
        """
        self.block_matrix = np.rot90(self.block_matrix, k=1, axes=(1,0))

    def check_collision(self, game_state):
        pass

    def move(self):
        pass