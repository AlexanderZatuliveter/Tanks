from typing import List
import pygame
from direction import Direction
from ex_sprite import ExSprite
from bullet import Bullet
from consts import BACKGROUND_COLOR, IS_DEBUG, SCREEN_HEIGHT, SCREEN_WIDTH, TANK_SPEED
from controls import Controls
from corner import Corner
from game_field import GameField
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
        start_corner: Corner,
        game_field: GameField
    ):
        super().__init__(image_path, x, y)

        self.rect = self.image.get_rect()

        self.controls = controls

        self.score = 0
        
        self.size = 50

        self.max_y = SCREEN_HEIGHT - self.rect.height / 2
        self.max_x = SCREEN_WIDTH - self.rect.width / 2

        self.min_y = self.rect.height / 2
        self.min_x = self.rect.width / 2

        self._next_shot_time = 0
        self.shot_speed_ms = 750
        self.speed = TANK_SPEED

        self.screen = screen
        self.angle: Direction

        self._bullets = bullets

        self.death_sound = "./sounds/death_sound.mp3"
        self.fire_sound = "./sounds/fire_sound.mp3"

        self.start_corner = start_corner
        self.game_field = game_field

    def play_sound(self, path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path)
        sound.play()

    def renew(self):
        self.play_sound(self.death_sound)
        if self.start_corner == Corner.top_left:
            self.x = self.min_x + self.speed
            self.y = self.min_y + self.speed
        if self.start_corner == Corner.top_right:
            self.x = self.max_x - self.speed
            self.y = self.min_y + self.speed
        if self.start_corner == Corner.down_right:
            self.x = self.max_x - self.speed
            self.y = self.max_y - self.speed
        if self.start_corner == Corner.down_left:
            self.x = self.min_x + self.speed
            self.y = self.max_y - self.speed

    def _modify_rect(self, difx, dify, rect: pygame.Rect):
        return pygame.Rect(difx+rect.x, dify+rect.y, rect.width, rect.height)

    def update(self):
        keys = pygame.key.get_pressed()
        rotated_rect = self.get_rotated_rect()

        if keys[self.controls.up_key] and self.y >= self.min_y + self.speed:
            x1 = rotated_rect.x
            x2 = rotated_rect.x + rotated_rect.width
            y = self.y - rotated_rect.height / 2 - self.speed
            rect = self._modify_rect(0, -self.speed, rotated_rect)
            if IS_DEBUG:
                pygame.draw.circle(self.screen, (200, 250, 0), (x1, y), 8, 1)
                pygame.draw.circle(self.screen, (200, 250, 0), (x2, y), 8, 1)
            self.angle = Direction.up
            if not self.game_field.colliderect_with(x1, y, rect) and not self.game_field.colliderect_with(x2, y, rect):
                self.y -= self.speed

        elif keys[self.controls.down_key] and self.y <= self.max_y - self.speed:
            x1 = rotated_rect.x
            x2 = rotated_rect.x + rotated_rect.width
            y = self.y + rotated_rect.height / 2 + self.speed
            rect = self._modify_rect(0, +self.speed, rotated_rect)
            if IS_DEBUG:
                pygame.draw.circle(self.screen, (200, 250, 0), (x1, y), 8, 1)
                pygame.draw.circle(self.screen, (200, 250, 0), (x2, y), 8, 1)
            self.angle = Direction.down
            if not self.game_field.colliderect_with(x1, y, rect) and not self.game_field.colliderect_with(x2, y, rect):
                self.y += self.speed

        elif keys[self.controls.left_key] and self.x >= self.min_x + self.speed:
            x = self.x - rotated_rect.width / 2 - self.speed
            y1 = rotated_rect.y
            y2 = rotated_rect.y + rotated_rect.height
            rect = self._modify_rect(-self.speed, 0, rotated_rect)
            if IS_DEBUG:
                pygame.draw.circle(self.screen, (200, 250, 0), (x, y1), 8, 1)
                pygame.draw.circle(self.screen, (200, 250, 0), (x, y2), 8, 1)
            self.angle = Direction.left
            if not self.game_field.colliderect_with(x, y1, rect) and not self.game_field.colliderect_with(x, y2, rect):
                self.x -= self.speed

        elif keys[self.controls.right_key] and self.x <= self.max_x - self.speed:
            x = self.x + rotated_rect.width / 2 + self.speed
            y1 = rotated_rect.y
            y2 = rotated_rect.y + rotated_rect.height
            rect = self._modify_rect(+self.speed, 0, rotated_rect)
            if IS_DEBUG:
                pygame.draw.circle(self.screen, (200, 250, 0), (x, y1), 8, 1)
                pygame.draw.circle(self.screen, (200, 250, 0), (x, y2), 8, 1)
            self.angle = Direction.right
            if not self.game_field.colliderect_with(x, y1, rect) and not self.game_field.colliderect_with(x, y2, rect):
                self.x += self.speed

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

    def score_on_screen(self, screen, pos_x, pos_y, text, rect):
        pygame.draw.rect(screen, BACKGROUND_COLOR, (pos_x, pos_y,
                                                    rect.width+30, rect.height+30))
        screen.blit(text, (pos_x, pos_y))
