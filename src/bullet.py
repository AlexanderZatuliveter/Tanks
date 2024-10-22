from direction import Direction
from ex_sprite import ExSprite
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Bullet(ExSprite):
    def __init__(self, tank, x, y, direction: Direction, speed: float = 1.5):

        super().__init__('images/bullet.png', x, y, direction)

        self.speed = speed
        self.is_destroyed = False

        self.rect = self.get_rotated_rect()
        self.tank = tank

    def destroy(self):
        self.is_destroyed = True

    def update(self):
        if self.angle == Direction.left:
            self.x -= self.speed
        if self.angle == Direction.right:
            self.x += self.speed
        if self.angle == Direction.up:
            self.y -= self.speed
        if self.angle == Direction.down:
            self.y += self.speed

        if self.x >= SCREEN_WIDTH:
            self.is_destroyed = True
        if self.y >= SCREEN_HEIGHT:
            self.is_destroyed = True
        if self.x <= 0:
            self.is_destroyed = True
        if self.y <= 0:
            self.is_destroyed = True
