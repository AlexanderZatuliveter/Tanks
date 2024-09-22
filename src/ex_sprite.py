import pygame
from consts import IS_DEBUG


class ExSprite:

    def __init__(self, image_path: str, x: float = 0, y: float = 0, angle: float = 0):
        # x, y - center of sprite
        self.x = x
        self.y = y
        # Load an image
        self.image = pygame.image.load(image_path)
        self.__angle = 0
        self.angle = angle

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if not self.__angle or self.__angle != value:
            self.__angle = value
            self.__rotated_image = pygame.transform.rotate(self.image, self.angle)

    def get_rotated_rect(self):
        return self.__rotated_image.get_rect(center=(self.x, self.y))

    def draw(self, screen: pygame.Surface):
        rotated_rect = self.get_rotated_rect()

        screen.blit(self.__rotated_image, rotated_rect.topleft)
        if IS_DEBUG:
            pygame.draw.circle(screen, (200, 0, 0), rotated_rect.topleft, 10, 1)
            pygame.draw.circle(screen, (0, 220, 0), rotated_rect.center, 10, 1)
            pygame.draw.rect(screen, (0, 0, 220), rotated_rect, 1)
            pygame.draw.circle(screen, (100, 220, 150), (self.x, self.y), 6.0, 1)
