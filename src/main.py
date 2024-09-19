import pygame
import sys
from blue_tank import Blue_Tank
from red_tank import Red_Tank

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1100

bg_color = 128, 128, 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

blue_tank = Blue_Tank(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH - 75, SCREEN_HEIGHT - 75, screen)
red_tank = Red_Tank(SCREEN_WIDTH//3, SCREEN_HEIGHT//3, SCREEN_WIDTH - 75, SCREEN_HEIGHT - 75)

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
    red_tank.draw(screen)
    
    pygame.display.flip()