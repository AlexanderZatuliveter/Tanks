from typing import List
import pygame
from direction import Direction
from utils import Utils
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Blue_Tank():
    def __init__(self, x, y, screen, bullets: List):

        utils = Utils()

        self.x = x
        self.y = y

        self.max_y = SCREEN_HEIGHT - 75
        self.max_x = SCREEN_WIDTH - 75

        self._next_shot_time = 0
        self.shot_speed_ms = 750
        self.speed = 0.6
        self.direction = Direction.right

        self.image = utils.load_image('images/blue_tank.png')
        self.rect = self.image.get_rect()

        self.screen = screen

        self._bullets = bullets

    def draw(self):
        image = pygame.transform.rotate(self.image, self.direction.value)
        self.screen.blit(image, (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y >= 0:
            self.y -= self.speed
            self.direction = Direction.up
        elif keys[pygame.K_s] and self.y <= self.max_y:
            self.y += self.speed
            self.direction = Direction.down
        elif keys[pygame.K_a] and self.x >= 0:
            self.x -= self.speed
            self.direction = Direction.left
        elif keys[pygame.K_d] and self.x <= self.max_x:
            self.x += self.speed
            self.direction = Direction.right

        if keys[pygame.K_LSHIFT]:
            if self._next_shot_time <= pygame.time.get_ticks():
                new_bullet = Bullet(self.x, self.y, self.direction)
                self._bullets.append(new_bullet)
                self._next_shot_time = pygame.time.get_ticks() + self.shot_speed_ms
