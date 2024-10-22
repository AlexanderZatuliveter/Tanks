import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((640, 480))

# Определение цвета (RGB)
white = (255, 255, 255)
black = (0, 0, 0)

# Инициализация шрифта (None означает системный шрифт по умолчанию, 36 - размер шрифта)
font = pygame.font.Font(None, 36)

# Создаем поверхность с текстом
text_surface = font.render("Привет, Pygame!", True, white)

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Закрашиваем экран черным цветом
    screen.fill(black)

    # Отображаем текст на экране (по координатам 100, 100)
    screen.blit(text_surface, (100, 100))

    # Обновляем экран
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
