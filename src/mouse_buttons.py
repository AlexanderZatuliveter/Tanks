import pygame
from game_field import GameField
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT


class Mouse:
    def __init__(self):
        self.blocks = []

    def update(self, game_field: GameField):
        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if left:
            game_field.put_block_by_screen_pos(mouse_x, mouse_y)
        if right:
            game_field.hit_block_by_screen_pos(mouse_x, mouse_y)
