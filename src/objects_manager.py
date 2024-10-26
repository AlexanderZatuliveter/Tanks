
from typing import List

import pygame


class ObjectsManager():
    def __init__(self):
        # self.__objects: List = []
        self.__all_sprites = pygame.sprite.Group()

    def _cleanup(self):
        for obj in self.__all_sprites:
            if obj.is_destroyed:
                self.__all_sprites.remove(obj)

    def update(self):
        self._cleanup()
        for obj in self.__all_sprites:
            obj.update()

    def draw_background(self, screen):
        for obj in self.__all_sprites:
            obj.draw_background(screen)

    def draw(self, screen):
        for obj in self.__all_sprites:
            obj.draw(screen)

    def get_object(self, obj_type):
        return [obj for obj in self.__all_sprites if isinstance(obj, obj_type)]

    def append(self, obj):
        self.__all_sprites.add(obj)
