import pygame
from consts import BACKGROUND_COLOR, IS_DEBUG
from image_loader import ImageLoader
from position import Position


class ExSprite(pygame.sprite.Sprite):

    def __init__(self, image_path: str, x: float = 0, y: float = 0, angle: float = 0):
        super().__init__()
        # x, y - center of sprite
        self.x = x
        self.y = y
        # Load an image
        self.image = ImageLoader.get_image(image_path)
        self.__angle = 0
        self.angle = angle

    @property
    def pos(self):
        return Position(self.x, self.y)

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

    def draw_background(self, screen: pygame.Surface):
        size = 100
        rect = self.get_rotated_rect()
        new_width = rect.width + size
        new_height = rect.height + size
        new_x = rect.x - size / 2
        new_y = rect.y - size / 2
        rect = pygame.Rect(new_x, new_y, new_width, new_height)
        pygame.draw.rect(screen, BACKGROUND_COLOR, rect)  # (new_x, new_y, new_width, new_height))
