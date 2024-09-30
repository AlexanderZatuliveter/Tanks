
from typing import List


class ObjectsManager():
    def __init__(self):
        self.__objects: List = []

    def _cleanup(self):
        for obj in self.__objects:
            if obj.is_destroyed:
                self.__objects.remove(obj)

    def update(self):
        self._cleanup()
        for obj in self.__objects:
            obj.update()

    def draw(self, screen):
        for obj in self.__objects:
            obj.draw(screen)

    def get_object(self, obj_type):
        return [obj for obj in self.__objects if isinstance(obj, obj_type)]

    def append(self, obj):
        self.__objects.append(obj)
