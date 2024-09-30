import pygame


class KaBoom:
    def __init__(self, pos):
        self.frames = [
            pygame.image.load('./images/kaboom1.png'),
            pygame.image.load('./images/kaboom2.png'),
            pygame.image.load('./images/kaboom3.png')
        ]
        self.frame_speed_ms = 100
        self._start_time = pygame.time.get_ticks()
        self._frame = 0
        self._pos = pos
        self.is_destroyed = False

    def update(self):
        duration = pygame.time.get_ticks() - self._start_time
        self._frame = duration // self.frame_speed_ms
        if (self._frame > 2):
            self.is_destroyed = True
        self._frame = min(self._frame, 2)

    def draw(self, screen):
        frame_image = self.frames[self._frame]
        rect = frame_image.get_rect()
        screen.blit(frame_image, (self._pos.x - rect.width / 2, self._pos.y - rect.height / 2))
