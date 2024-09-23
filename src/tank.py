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

        self.max_y = SCREEN_HEIGHT - 30
        self.max_x = SCREEN_WIDTH

        self.min_y = 30
        self.min_x = 30

        self._next_shot_time = 0
        self.shot_speed_ms = 750
        self.speed = 0.6

        self.screen = screen
        self.angle: Direction

        self._bullets = bullets

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls.up_key] and self.y >= self.min_y:
            self.y -= self.speed
            self.angle = Direction.up
        elif keys[self.controls.down_key] and self.y <= self.max_y:
            self.y += self.speed
            self.angle = Direction.down
        elif keys[self.controls.left_key] and self.x >= self.min_x:
            self.x -= self.speed
            self.angle = Direction.left
        elif keys[self.controls.right_key] and self.x <= self.max_x:
            self.x += self.speed
            self.angle = Direction.right
        if keys[self.controls.fire]:
            self._fire()

    def _fire(self):
        if self._next_shot_time <= pygame.time.get_ticks():
            rect = self.get_rotated_rect()
            if self.angle == Direction.up:
                new_bullet = Bullet(self.x, self.y - rect.height / 2, self.angle)
                self._bullets.append(new_bullet)
            elif self.angle == Direction.down:
                new_bullet = Bullet(self.x, self.y + rect.height / 2, self.angle)
                self._bullets.append(new_bullet)
            elif self.angle == Direction.left:
                new_bullet = Bullet(self.x - rect.width / 2, self.y, self.angle)
                self._bullets.append(new_bullet)
            elif self.angle == Direction.right:
                new_bullet = Bullet(self.x + rect.width / 2, self.y, self.angle)
                self._bullets.append(new_bullet)

            self._next_shot_time = pygame.time.get_ticks() + self.shot_speed_ms
