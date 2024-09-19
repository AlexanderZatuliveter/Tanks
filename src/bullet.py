import pygame
from utils import Utils


class Bullet():
    def __init__(self, x, y):

        utils = Utils()

        self.x = x
        self.y = y

        self.image = utils.load_image('images/bullet2.png')
        self.rect = self.image.get_rect()

        self.angle = 0

    def draw(self, screen, angle):
        image = pygame.transform.rotate(self.image, angle)
        screen.blit(image, (self.x, self.y))

    def shoot(self, screen, angle, max_x, max_y):
        self.draw(screen, angle)
        while True:
            self.x += 1
            if self.x >= max_x:
                break
            if self.y >= max_y:
                break
