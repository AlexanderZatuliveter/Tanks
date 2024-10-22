from typing import List
import pygame
from direction import Direction
from ex_sprite import ExSprite
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from controls import Controls
from corner import Corner
from objects_manager import ObjectsManager


class Tank(ExSprite):
    def __init__(
        self,
        x: float,
        y: float,
        screen: pygame.Surface,
        bullets: ObjectsManager,
        image_path: str,
        controls: Controls,
        start_corner: Corner
    ):
        super().__init__(image_path, x, y)

        self.rect = self.image.get_rect()

        self.controls = controls

        self.score = 0

        self.max_y = SCREEN_HEIGHT - self.rect.height / 2
        self.max_x = SCREEN_WIDTH - self.rect.width / 2

        self.min_y = self.rect.height / 2
        self.min_x = self.rect.width / 2

        self._next_shot_time = 0
        self.shot_speed_ms = 750
        self.speed = 0.4

        self.screen = screen
        self.angle: Direction

        self._bullets = bullets

        self.death_sound = "./sounds/death_sound.mp3"
        self.fire_sound = "./sounds/fire_sound.mp3"

        self.start_corner = start_corner

    def play_sound(self, path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path)
        sound.play()

    def renew(self):
        self.play_sound(self.death_sound)
        if self.start_corner == Corner.top_left:
            self.x = self.min_x
            self.y = self.min_y
        if self.start_corner == Corner.top_right:
            self.x = self.max_x
            self.y = self.min_y
        if self.start_corner == Corner.down_right:
            self.x = self.max_x
            self.y = self.max_y
        if self.start_corner == Corner.down_left:
            self.x = self.min_x
            self.y = self.max_y

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

    def score_plus_one(self):
        self.score += 1

    def _fire(self):
        if self._next_shot_time <= pygame.time.get_ticks():
            rect = self.get_rotated_rect()
            if self.angle == Direction.up:
                new_bullet = Bullet(self, self.x, self.y - rect.height / 2, self.angle)
                self._bullets.append(new_bullet)
                self.play_sound(self.fire_sound)
            elif self.angle == Direction.down:
                new_bullet = Bullet(self, self.x, self.y + rect.height / 2, self.angle)
                self._bullets.append(new_bullet)
                self.play_sound(self.fire_sound)
            elif self.angle == Direction.left:
                new_bullet = Bullet(self, self.x - rect.width / 2, self.y, self.angle)
                self._bullets.append(new_bullet)
                self.play_sound(self.fire_sound)
            elif self.angle == Direction.right:
                new_bullet = Bullet(self, self.x + rect.width / 2, self.y, self.angle)
                self._bullets.append(new_bullet)
                self.play_sound(self.fire_sound)

            self._next_shot_time = pygame.time.get_ticks() + self.shot_speed_ms
