import random

class Block():
    def __init__(self):
        self.blocks = {"O":[[1,1],[1,1]],
                        "Z":[[2,2,0],[0,2,2],[0,0,0]],
                        "S":[[0,3,3],[3,3,0],[0,0,0]],
                        "I":[[0,0,0,0],[4,4,4,4],[0,0,0,0],[0,0,0,0]],
                        "T":[[0,5,0],[5,5,5],[0,0,0]],
                        "J":[[6,0,0],[6,6,6],[0,0,0]],
                        "L":[[0,0,7],[7,7,7],[0,0,0]],}
    
    def get_random_block(self):
        """
        Returns:
            Random block from the list 
        """
        key = random.choice(self.blocks.keys())
        return (key,self.blocks[key])