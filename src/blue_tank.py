import pygame
from utils import Utils
from bullet import Bullet


class Blue_Tank():
    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT, screen):

        utils = Utils()

        self.x = x
        self.y = y

        self.max_y = SCREEN_HEIGHT
        self.max_x = SCREEN_WIDTH

        self.bullet = Bullet(self.x, self.y)

        self.speed = 0.6
        self.angle = 0

        self.image = utils.load_image('images/blue_tank.png')
        self.rect = self.image.get_rect()

        self.screen = screen

    def draw(self):
        image = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(image, (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y >= 0:
            self.y -= self.speed
            self.angle = 180
        if keys[pygame.K_s] and self.y <= self.max_y:
            self.y += self.speed
            self.angle = 0
        if keys[pygame.K_a] and self.x >= 0:
            self.x -= self.speed
            self.angle = 270
        if keys[pygame.K_d] and self.x <= self.max_x:
            self.x += self.speed
            self.angle = 90

        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.angle = 225
        if keys[pygame.K_s] and keys[pygame.K_d]:
            self.angle = 45
        if keys[pygame.K_w] and keys[pygame.K_d]:
            self.angle = 135
        if keys[pygame.K_s] and keys[pygame.K_a]:
            self.angle = 315

        if keys[pygame.K_LSHIFT]:
            self.bullet.shoot(self.screen, self.angle, self.max_x, self.max_y)
