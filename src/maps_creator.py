import sys
import pygame
from consts import GAME_FIELD_HEIGHT, GAME_FIELD_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT
from mouse_buttons import Mouse
from game_field import GameField


pygame.init()

bg_color = 200, 200, 200

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

mouse = Mouse()

game_field = GameField(GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)

while True:
    screen.fill(bg_color)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            print(f"blocks:{mouse.blocks}")
            pygame.quit()
            sys.exit()
        if keys[pygame.K_s]:
            print('saved')
            game_field.save_to_file()

        if keys[pygame.K_l]:
            print('loaded')
            game_field.load_from_file()

    game_field.draw(screen)

    mouse.update(game_field)

    pygame.display.update()
