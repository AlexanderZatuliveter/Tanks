import pygame

from image_loader import ImageLoader


class Block(pygame.sprite.Sprite):

    def __init__(self):

        self.size = 50

        self.image = ImageLoader.get_image('./images/block.png')
        self.rect = self.image.get_rect()

        self.is_destroyed = False

    def destroy(self):
        self.is_destroyed = True

    def draw(self, screen, pos):
        if not self.is_destroyed:
            screen.blit(self.image, pos)
