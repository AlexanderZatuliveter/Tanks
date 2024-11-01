import numpy as np
import pygame
from block import Block
from consts import IS_DEBUG
from position import IntPosition
import json


class GameField:
    def __init__(self, x, y):
        self.__block_size = 50
        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)

    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            if block and block.is_destroyed:
                self.field[x, y] = None

    def draw(self, screen):
        for (bx, by), block in np.ndenumerate(self.field):
            if block:
                pos = self._get_block_position(bx, by)
                block.draw(screen, pos)
                if IS_DEBUG:
                    pygame.draw.rect(screen, (0, 0, 220), self._get_block_rect(bx, by), 1)

    def _get_block_position(self, bx, by):
        return (
            bx * self.__block_size,
            by * self.__block_size
        )

    def get_block_field_position(self, x: float, y: float):
        return IntPosition(
            int(x // self.__block_size),
            int(y // self.__block_size)
        )

    def _get_block_rect(self, x: int, y: int):
        return pygame.Rect(x * self.__block_size, y * self.__block_size, self.__block_size, self.__block_size)

    def colliderect_with(self, x, y, rect: pygame.Rect):
        block_pos = self.get_block_field_position(x, y)
        
        if 0 <= block_pos.x < len(self.field) and 0 <= block_pos.y < len(self.field[0]):
            block = self.field[block_pos.x][block_pos.y]
            if block and rect.colliderect(self._get_block_rect(block_pos.x, block_pos.y)):
                return True
            
        return False

    def _colliderect_with(self, rect: pygame.Rect):
        block_pos = self.get_block_field_position(rect.x, rect.y)
        block = self.field[block_pos.x][block_pos.y]
        if block and rect.colliderect(block_pos.x * self.__block_size, block_pos.y * self.__block_size, block.rect.width, block.rect.height):
            return True
        return False

    def put_block_by_screen_pos(self, x, y):
        pos = self.get_block_field_position(x, y)
        self.put_block(pos)

    def put_block(self, pos: IntPosition):
        block = self.field[pos.x][pos.y]
        if not block:
            self.field[pos.x][pos.y] = Block()

    def hit_block(self, pos: IntPosition):
        block = self.field[pos.x][pos.y]
        if block:
            self.field[pos.x][pos.y] = None

    def hit_block_by_screen_pos(self, x, y):
        pos = self.get_block_field_position(x, y)
        self.hit_block(pos)

    def save_to_file(self):
        map = {}
        positions = {}
        for (x, y), block in np.ndenumerate(self.field):
            if isinstance(block, Block):
                positions[str(IntPosition(x, y))] = type(block).__name__
        map["positions"] = positions
        json_string = json.dumps(map, indent=2)
        with open("first.tankmap", "w") as json_file:
            json_file.write(json_string)

    def load_from_file(self):
        with open("first.tankmap", "r") as json_file:
            json_string = json_file.read()

        map_data = json.loads(json_string)

        # Initialize or clear the field
        self.field = np.empty_like(self.field)

        # Access the "positions" dictionary within the loaded map_data
        positions = map_data.get("positions", {})

        for pos_str, block_type in positions.items():
            # Convert pos_str back to an IntPosition instance
            pos = IntPosition.from_string(pos_str)
            self.put_block(pos)
