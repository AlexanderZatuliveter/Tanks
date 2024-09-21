from typing import List
import pygame
from direction import Direction
from ex_sprite import ExSprite
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from controls import Controls


class Tank(ExSprite):
    def __init__(self, x, y, screen, bullets: List, image_path: str, controls: Controls):

        super().__init__(image_path, x, y)

        self.controls = controls

        self.max_y = SCREEN_HEIGHT - 75
        self.max_x = SCREEN_WIDTH - 75

        self._next_shot_time = 0
        self.shot_speed_ms = 750
        self.speed = 0.6

        self.screen = screen

        self._bullets = bullets

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls.up_key] and self.y >= 0:
            self.y -= self.speed
            self.angle = Direction.up
        elif keys[self.controls.down_key] and self.y <= self.max_y:
            self.y += self.speed
            self.angle = Direction.down
        elif keys[self.controls.left_key] and self.x >= 0:
            self.x -= self.speed
            self.angle = Direction.left
        elif keys[self.controls.right_key] and self.x <= self.max_x:
            self.x += self.speed
            self.angle = Direction.right
        if keys[self.controls.fire]:
            self._fire()

    def _fire(self):
        if self._next_shot_time <= pygame.time.get_ticks():
            new_bullet = Bullet(self.x, self.y, self.angle)
            self._bullets.append(new_bullet)
            self._next_shot_time = pygame.time.get_ticks() + self.shot_speed_ms
