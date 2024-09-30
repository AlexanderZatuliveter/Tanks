import pygame
import numpy as np
from block import Block
from consts import HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT

class GameField:
    def __init__(self, x, y):
        self.block = Block(x, y)
        
        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)
        
    def draw_block(self, x, y, screen):
        self.field[x][y] = screen.blit(self.block.image, (x, y))
        