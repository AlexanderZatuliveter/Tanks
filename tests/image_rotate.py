
import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load an image
image = pygame.image.load('./images/bullet.png')

# Set the image's rectangle
image_rect = image.get_rect(center=(400, 300))

# Angle of rotation
angle = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    # Increase the angle for the next frame (counterclockwise)
    angle += 1
    if angle >= 360:
        angle = 0

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rotated image
    screen.blit(rotated_image, rotated_rect.topleft)
    pygame.draw.circle(screen, (200, 0, 0), rotated_rect.topleft, 5)
    pygame.draw.circle(screen, (0, 220, 0), rotated_rect.center, 5)
    pygame.draw.rect(screen, (0, 0, 220), rotated_rect, 1)
    pygame.draw.rect(screen, (0, 230, 220), image_rect, 1)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
