import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анімація зображення зліва направо")

# Завантаження зображення
image = pygame.image.load("image.png")
image_rect = image.get_rect()
image_rect.y = HEIGHT // 2 - image_rect.height // 2  # По центру вертикалі

# Швидкість руху
speed = 5

# Головний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очищення екрану
    screen.fill((255, 255, 255))  # Білий фон

    # Переміщення зображення вправо
    image_rect.x += speed
    if image_rect.x > WIDTH:
        image_rect.x = -image_rect.width  # Почати зліва знову

    # Малювання зображення
    screen.blit(image, image_rect)

    # Оновлення екрану
    pygame.display.flip()

    # Затримка кадру
    pygame.time.Clock().tick(60)

# Завершення
pygame.quit()
sys.exit()
