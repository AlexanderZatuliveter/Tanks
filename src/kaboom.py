import pygame


class KaBoom:
    def __init__(self):
        self.frame1 = pygame.image.load('./images/kaboom1.png')
        self.frame2 = pygame.image.load('./images/kaboom2.png')
        self.frame3 = pygame.image.load('./images/kaboom3.png')
        
    def draw(self, screen, pos):
        screen.blit(self.frame1, pos)
        screen.blit(self.frame2, pos)
        screen.blit(self.frame3, pos)