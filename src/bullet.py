import pygame
from direction import Direction
from ex_sprite import ExSprite
from utils import Utils
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Bullet():
    def __init__(self, x, y, direction: Direction, speed: float = 0.260):

        utils = Utils()

        self.x = x
        self.y = y

        self.speed = speed

        self.sprite = ExSprite('images/bullet.png')
        # self.image = utils.load_image('images/bullet.png')
        # self.rect = self.image.get_rect()

        self.direction = direction

        self.is_destroyed = False

    def draw(self, screen: pygame.Surface):
        self.sprite.draw(screen)
        # image = pygame.transform.rotate(self.image, self.direction)
        # screen.blit(image, (self.x - self.rect.centerx, self.y - self.rect.centery))
        # pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 10)

    def update(self):
        if self.direction == Direction.left:
            self.x -= self.speed
        if self.direction == Direction.right:
            self.x += self.speed
        if self.direction == Direction.up:
            self.y -= self.speed
        if self.direction == Direction.down:
            self.y += self.speed

        self.sprite.angle = self.direction.value
        self.sprite.x = self.x
        self.sprite.y = self.y

        if self.x >= SCREEN_WIDTH:
            self.is_destroyed = True
        if self.y >= SCREEN_HEIGHT:
            self.is_destroyed = True
        if self.x <= 0:
            self.is_destroyed = True
        if self.y <= 0:
            self.is_destroyed = True
