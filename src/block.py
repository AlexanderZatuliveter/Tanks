import pygame

from image_loader import ImageLoader


class Block(pygame.sprite.Sprite):

    def __init__(self):
        self.image = ImageLoader.get_image('./images/block.png')
        self.rect = self.image.get_rect()
        # self.is_destroyed = False
        self._health = 4
        self._max_health = self._health
        self._crack_images = [pygame.image.load(f"images/block_cracks/crack{num}.png") for num in range(1, 5)]
        self.__crack_images_len = len(self._crack_images)

    @property
    def is_destroyed(self):
        return self._health <= 0

    def fire(self):
        self._health -= 2

    def draw(self, screen, pos):
        if not self.is_destroyed:
            screen.blit(self.image, pos)
            self.draw_cracks(screen, pos)

    def draw_cracks(self, screen, pos):
        fl = (self._health / self._max_health) * self.__crack_images_len
        number = self.__crack_images_len - int(fl)
        if number > 0:
            screen.blit(self._crack_images[number-1], pos)
