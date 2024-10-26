import numpy as np
from block import Block
from consts import BLOCK_SIZE
from position import IntPosition
import json


class GameField:
    def __init__(self, x, y):
        self.blocks = []

        self.__block_size = 50

        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)

        # for i in range(x):
        #     self.field[i][0] = Block()
        #     self.field[i][y-1] = Block()

        # for j in range(y):
        #     if j != 0 and j != y-1:
        #         self.field[0][j] = Block()
        #         self.field[x-1][j] = Block()

    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            if block is not None:
                block.update()

    def draw(self, screen):
        for (bx, by), block in np.ndenumerate(self.field):
            if block:
                pos = self._get_block_position(bx, by)
                block.draw(screen, pos)

    def _get_block_position(self, bx, by):
        return (
            bx * self.__block_size,
            by * self.__block_size
        )

    def get_block_field_position(self, x, y):
        return IntPosition(
            int(x // self.__block_size),
            int(y // self.__block_size)
        )

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
