import pygame

class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.size = 50
        
        self.image = pygame.image.load('./images/block.png')
        self.rect = self.image.get_rect()