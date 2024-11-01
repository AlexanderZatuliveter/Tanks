import pygame

from consts import BACKGROUND_COLOR


class KaBoom(pygame.sprite.Sprite):
    def __init__(self, pos, frames_type):
        super().__init__()
        if frames_type == "tank":
            self.frames = [pygame.image.load(f'./images/tank_explosion/{n}.png') for n in range(1, 7)]
            self.frame_speed_ms = 45
        elif frames_type == "block":
            self.frames = [pygame.image.load(f'./images/block_explosion/{n}.png') for n in range(1, 10)]
            self.frame_speed_ms = 30
        else:
            raise Exception(f"Unknown frame type. {frames_type=}")
        self._start_time = pygame.time.get_ticks()
        self._frame = 0
        self._pos = pos
        self.is_destroyed = False
        self._frames_count = len(self.frames)

    def update(self):
        duration = pygame.time.get_ticks() - self._start_time
        self._frame = duration // self.frame_speed_ms
        if (self._frame > self._frames_count):
            self.is_destroyed = True
        self._frame = min(self._frame, self._frames_count - 1)

    def draw(self, screen):
        frame_image = self.frames[self._frame]
        rect = frame_image.get_rect()
        screen.blit(frame_image, (self._pos.x - rect.width / 2, self._pos.y - rect.height / 2))

    def draw_background(self, screen):
        frame_image = self.frames[self._frames_count-1]
        rect = frame_image.get_rect()
        pygame.draw.rect(screen, BACKGROUND_COLOR, (self._pos.x - rect.width / 2,
                         self._pos.y - rect.height / 2, rect.width, rect.height))
