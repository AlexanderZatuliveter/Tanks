import pygame


class ExSprite:

    def __init__(self, image_path: str, x: float = 0, y: float = 0, angle: float = 0):
        # x, y - center of sprite
        self.x = x
        self.y = y
        self.angle = angle  # rotate angle
        # Load an image
        self.image = pygame.image.load(image_path)

        # todo: if you need image rect, just create a new calculated property
        # self.image_rect = self.image.get_rect(center=(x, y))

        self.debug = True  # debug mode, shows additional points of the sprite

    def draw(self, screen: pygame.Surface):
        # image_rect = self.image.get_rect(center=(self.x, self.y))
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=(self.x, self.y))

        screen.blit(rotated_image, rotated_rect.topleft)
        if self.debug:
            pygame.draw.circle(screen, (200, 0, 0), rotated_rect.topleft, 10, 1)
            pygame.draw.circle(screen, (0, 220, 0), rotated_rect.center, 10, 1)
            pygame.draw.rect(screen, (0, 0, 220), rotated_rect, 1)
            pygame.draw.circle(screen, (100, 220, 150), (self.x, self.y), 6.0, 1)
