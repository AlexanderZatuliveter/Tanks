import pygame

# Инициализация Pygame
pygame.init()

# Инициализация микшера для работы со звуком
pygame.mixer.init()

# Загрузка звукового файла
sound = pygame.mixer.Sound("./sounds/tankDrive_sound.mp3")

# Воспроизведение звука
sound.play()

# Чтобы задержать программу, пока звук играет, используем задержку
pygame.time.delay(int(sound.get_length() * 1000))

# Завершение работы с Pygame
pygame.quit()
