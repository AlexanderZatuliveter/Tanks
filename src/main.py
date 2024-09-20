from typing import List
import pygame
import sys
from tank import Tank
from bullet import Bullet
from consts import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

bg_color = 128, 128, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bullets: List[Bullet] = list()

blue_tank = Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen, bullets, player=1)
red_tank = Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, screen, bullets, player=2)


while True:
    screen.fill(bg_color)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    blue_tank.update()
    blue_tank.draw()

    red_tank.update()
    red_tank.draw()

    for bullet in bullets:
        if bullet.is_destroyed:
            bullets.remove(bullet)

    for bullet in bullets:
        bullet.update()
        bullet.draw(screen)

    pygame.display.flip()
