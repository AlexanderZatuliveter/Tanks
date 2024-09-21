from typing import List
import pygame
from direction import Direction
from ex_sprite import ExSprite
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from controls import Controls


class Tank(ExSprite):
    def __init__(self, x, y, screen, bullets: List, player: int):

        if player == 1:
            super().__init__('images/blue_tank.png', x, y)
            self.controls = Controls(
                up_key=pygame.K_w,
                down_key=pygame.K_s,
                left_key=pygame.K_a,
                right_key=pygame.K_d,
                fire=pygame.K_LSHIFT
            )
        else:
            super().__init__('images/red_tank.png', x, y)
            self.controls = Controls(
                up_key=pygame.K_UP,
                down_key=pygame.K_DOWN,
                left_key=pygame.K_LEFT,
                right_key=pygame.K_RIGHT,
                fire=pygame.K_RCTRL
            )

        self._player = player

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
