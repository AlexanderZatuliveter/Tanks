
import os
import pygame


class Utils():
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def load_image(self, relative_path):
        return pygame.image.load(os.path.join(self.base_path, relative_path))
