import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self):       
        self.size = 50
        
        self.image = pygame.image.load('./images/block.png')
        self.rect = self.image.get_rect()
        
        self.is_destroyed = False
        
    def destroy(self):
        self.is_destroyed = True
        
    def draw(self, screen, pos):
        if self.is_destroyed == False:
            screen.blit(self.image, pos)