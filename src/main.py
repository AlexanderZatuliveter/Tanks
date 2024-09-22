from typing import List
import pygame
import sys
from controls import Controls
from tank import Tank
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

bg_color = 128, 128, 0

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bullets: List[Bullet] = list()

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


blue_tank = Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen, bullets, 'images/blue_tank.png', player1_controls)
red_tank = Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen, bullets, 'images/red_tank.png', player2_controls)
green_tank = Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen, bullets, 'images/green_tank.png', player3_controls)

tanks = [blue_tank, red_tank, green_tank]

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

    for bullet in bullets:
        if bullet.is_destroyed:
            bullets.remove(bullet)

    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)

        # if blue_tank..collidepoint(bullet.x, bullet.y):
        #     tanks.remove(blue_tank)

    pygame.display.flip()
