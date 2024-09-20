import pygame
from direction import Direction
from utils import Utils
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Bullet():
    def __init__(self, x, y, direction: Direction, speed: float = 2.0):

        utils = Utils()

        self.x = x+30
        self.y = y+30

        self.speed = speed

        self.image = utils.load_image('images/bullet.png')
        self.rect = self.image.get_rect()

        self.direction = direction

        self.is_destroyed = False

    def draw(self, screen):
        image = pygame.transform.rotate(self.image, self.direction)
        screen.blit(image, (self.x, self.y))

    def update(self):
        if self.direction == Direction.left:
            self.x -= self.speed
        if self.direction == Direction.right:
            self.x += self.speed
        if self.direction == Direction.up:
            self.y -= self.speed
        if self.direction == Direction.down:
            self.y += self.speed

        if self.x >= SCREEN_WIDTH:
            self.is_destroyed = True
        if self.y >= SCREEN_HEIGHT:
            self.is_destroyed = True
        if self.x <= 0:
            self.is_destroyed = True
        if self.y <= 0:
            self.is_destroyed = True
