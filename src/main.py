from typing import List
import pygame
import sys
from controls import Controls
from game_field import GameField
from kaboom import KaBoom
from objects_manager import ObjectsManager
from tank import Tank
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT
from corner import Corner

pygame.init()

bg_color = 128, 128, 0

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

other_objects = ObjectsManager()

player1_controls = Controls(
    up_key=pygame.K_w,
    down_key=pygame.K_s,
    left_key=pygame.K_a,
    right_key=pygame.K_d,
    fire=pygame.K_LSHIFT
)

player2_controls = Controls(
    up_key=pygame.K_UP,
    down_key=pygame.K_DOWN,
    left_key=pygame.K_LEFT,
    right_key=pygame.K_RIGHT,
    fire=pygame.K_RCTRL
)

player3_controls = Controls(
    up_key=pygame.K_i,
    down_key=pygame.K_k,
    left_key=pygame.K_j,
    right_key=pygame.K_l,
    fire=pygame.K_h
)


blue_tank = Tank(
    x=SCREEN_WIDTH//2.25,
    y=SCREEN_HEIGHT//2.25,
    screen=screen,
    bullets=other_objects,
    image_path='images/blue_tank.png',
    controls=player1_controls,
    start_corner=Corner.top_left
)

red_tank = Tank(
    x=SCREEN_WIDTH//2.25,
    y=SCREEN_HEIGHT//2.25,
    screen=screen,
    bullets=other_objects,
    image_path='images/red_tank.png',
    controls=player2_controls,
    start_corner=Corner.top_right
)

green_tank = Tank(
    x=SCREEN_WIDTH//2.25,
    y=SCREEN_HEIGHT//2.25,
    screen=screen,
    bullets=other_objects,
    image_path='images/green_tank.png',
    controls=player3_controls,
    start_corner=Corner.down_right
)

tanks = [blue_tank, red_tank, green_tank]

game_field = GameField(50, 33)


while True:
    screen.fill(bg_color)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for tank in tanks:
        tank.draw(screen)
        tank.update()

    other_objects.draw(screen)
    other_objects.update()

    for bullet in other_objects.get_object(Bullet):
        for tank in tanks:
            if tank.get_rotated_rect().collidepoint(bullet.x, bullet.y):
                bullet.destroy()
                other_objects.append(KaBoom(tank.pos))
                tank.renew()

    game_field.draw_block(x=20, y=20, screen=screen)

    pygame.display.flip()
