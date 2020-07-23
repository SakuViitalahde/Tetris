import numpy as np

class Block():
    def __init__(self, block_matrix, shape):
        super().__init__()
        self.block_position = (1,4) if len(block_matrix) == 2 else (1,3) 
        self.block_matrix = block_matrix # This is 2x2,3x3 or 4x4 depending from blocktype
        self.shape = shape # Shape of block
        self.timer = 10
    
    def rotate_block(self):
        """
        Rotate Matrix 90 degrees clockwise
        """
        self.block_matrix = np.rot90(self.block_matrix, k=1, axes=(1,0))

    def check_collision(self, game_state):
        pass

    def move(self, game_state):
        """Move Block one space down
        
        Returns: True if able to move and False if not.
        """
        self.timer -= 1
        if self.timer <= 0:
            if not game_state.check_collision(self):
                self.block_position = (self.block_position[0] + 1, self.block_position[1])
                self.timer = 10
                return True
            else:
                return False
        return True
    
    def calculate_height(self):
        height = 0
        for row in self.block_matrix:
            if len(set(row)) > 1 or self.set_unpacking(set(row)) > 0:
                height += 1
        return height

    def set_unpacking(self, s):
        e, *_ = s
        return e