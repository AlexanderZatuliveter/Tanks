import pygame
from utils import Utils

class Red_Tank():
    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        utils = Utils()
        
        self.x = x
        self.y = y
        
        self.max_y = SCREEN_HEIGHT
        self.max_x = SCREEN_WIDTH
        
        self.speed = 0.6
        self.angle = 0
        
        self.image = utils.load_image('images/red_tank.png')
        self.rect = self.image.get_rect()
        
    def draw(self, screen):
            image = pygame.transform.rotate(self.image, self.angle)
            screen.blit(image, (self.x, self.y))
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP] and self.y >= 0:
            self.y -= self.speed
            self.angle = 180
        if keys [pygame.K_DOWN] and self.y <= self.max_y:
            self.y += self.speed
            self.angle = 0
        if keys [pygame.K_LEFT]  and self.x >= 0:
            self.x -= self.speed
            self.angle = 270
        if keys [pygame.K_RIGHT] and self.x <= self.max_x:
            self.x += self.speed
            self.angle = 90
            
        if keys [pygame.K_UP] and keys [pygame.K_LEFT]:
            self.angle = 225
        if keys [pygame.K_DOWN] and keys [pygame.K_RIGHT]:
            self.angle = 45
        if keys [pygame.K_UP] and keys [pygame.K_RIGHT]:
            self.angle = 135
        if keys [pygame.K_DOWN] and keys [pygame.K_LEFT]:
            self.angle = 315