import pygame
import numpy as np
from block import Block
from consts import BLOCK_SIZE


class GameField:
    def __init__(self, x, y, screen):
        
        self.__block_size = 50
        
        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)
        
        self.drawn_blocks = np.zeros((x, y), dtype=bool)
        

        for i in range(x):
            self.field[i][0] = Block()
            self.field[i][y-1] = Block()

        for j in range(y):
            if j != 0 and j != y-1:
                self.field[0][j] = Block()
                self.field[x-1][j] = Block()
        
            
    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            if block is not None:
                block.update()

    def draw(self, screen):
        for (bx, by), block in np.ndenumerate(self.field):
            if block is not None and not self.drawn_blocks[bx][by]:
                pos = self._get_block_position(bx, by)
                block.draw(screen, pos)
                self.drawn_blocks[bx][by] = True
                
    def _get_block_position(self, bx, by):
        return (
            bx * self.__block_size,
            by * self.__block_size
        )