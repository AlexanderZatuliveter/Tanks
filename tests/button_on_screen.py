import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройка экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Кнопка в Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Шрифт для текста на кнопке
font = pygame.font.Font(None, 36)

# Создание кнопки
button_rect = pygame.Rect(300, 250, 200, 50)  # (x, y, ширина, высота)
button_text = font.render("Нажми меня", True, WHITE)
button_text_rect = button_text.get_rect(center=button_rect.center)

# Основной игровой цикл
while True:
    screen.fill(GRAY)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Проверка нажатия на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                if button_rect.collidepoint(event.pos):
                    print("Кнопка нажата!")

    # Рисуем кнопку
    pygame.draw.rect(screen, DARK_GRAY if button_rect.collidepoint(pygame.mouse.get_pos()) else BLACK, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()