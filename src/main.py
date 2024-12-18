from typing import List
import pygame
import sys
from block import Block
from controls import Controls
from game_field import GameField
from kaboom import KaBoom
from objects_manager import ObjectsManager
from tank import Tank
from bullet import Bullet
from consts import BACKGROUND_COLOR, BLOCK_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT
from corner import Corner

pygame.init()

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

other_objects = ObjectsManager()

game_field = GameField(GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)

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
    fire=pygame.K_RSHIFT
)

player3_controls = Controls(
    up_key=pygame.K_i,
    down_key=pygame.K_k,
    left_key=pygame.K_j,
    right_key=pygame.K_l,
    fire=pygame.K_h
)


blue_tank = Tank(
    x=0+BLOCK_SIZE/2,
    y=0+BLOCK_SIZE/2,
    screen=screen,
    bullets=other_objects,
    image_path='images/blue_tank.png',
    controls=player1_controls,
    start_corner=Corner.top_left,
    game_field=game_field
)

red_tank = Tank(
    x=SCREEN_WIDTH-BLOCK_SIZE/2,
    y=0+BLOCK_SIZE/2,
    screen=screen,
    bullets=other_objects,
    image_path='images/red_tank.png',
    controls=player2_controls,
    start_corner=Corner.top_right,
    game_field=game_field
)

green_tank = Tank(
    x=SCREEN_WIDTH-BLOCK_SIZE/2,
    y=SCREEN_HEIGHT-BLOCK_SIZE/2,
    screen=screen,
    bullets=other_objects,
    image_path='images/green_tank.png',
    controls=player3_controls,
    start_corner=Corner.down_right,
    game_field=game_field
)

tanks = [blue_tank, red_tank, green_tank]

game_field.load_from_file()

font = pygame.font.Font("./fonts/NoizeSportFreeVertionRegular.ttf", 30)

block = Block()

clock = pygame.time.Clock()

screen.fill(BACKGROUND_COLOR)

while True:

    for tank in tanks:
        tank.draw_background(screen)

    other_objects.draw_background(screen)

    text_surface_green_tank = font.render(
        f"Green_score:{green_tank.score}", True, (0, 80, 0))
    text_surface_red_tank = font.render(
        f"Red_score:{red_tank.score}", True, (80, 0, 0))
    text_surface_blue_tank = font.render(
        f"Blue_score:{blue_tank.score}", True, (0, 0, 120))

    tank.score_on_screen(screen, SCREEN_WIDTH-325, SCREEN_HEIGHT-40,
                         text_surface_green_tank, text_surface_green_tank.get_rect())
    tank.score_on_screen(screen, SCREEN_WIDTH-300, 0,
                         text_surface_red_tank, text_surface_red_tank.get_rect())
    tank.score_on_screen(screen, 5, 0,
                         text_surface_blue_tank, text_surface_blue_tank.get_rect())

    game_field.update()
    game_field.draw(screen)  # todo: draw only once at the beginning, and draw only modified blocks.

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for tank in tanks:
        tank.draw(screen)
        tank.update()

    other_objects.update()
    other_objects.draw(screen)

    for bullet in other_objects.get_object(Bullet):
        for tank in tanks:
            if tank.get_rotated_rect().collidepoint(bullet.x, bullet.y):
                bullet.destroy()
                other_objects.append(KaBoom(tank.pos, "tank"))
                tank.renew()
                bullet.tank.score_plus_one()
        if game_field._colliderect_with(bullet.get_rotated_rect()):
            block_pos = game_field.get_block_field_position(bullet.x, bullet.y)
            block = game_field.field[block_pos.x][block_pos.y]
            if block:
                block.fire()
                bullet.destroy()
                if block._health <= 0:
                    other_objects.append(KaBoom(bullet.pos, "block"))
                    pygame.mixer.Sound("./sounds/death_sound.mp3").play()
        for bullet1 in other_objects.get_object(Bullet):
            for bullet2 in other_objects.get_object(Bullet):
                if bullet1 != bullet2 and bullet1.get_rotated_rect().colliderect(bullet2.get_rotated_rect()):
                    bullet1.destroy()
                    bullet2.destroy()
                    
    pygame.display.flip()
    clock.tick(60)
