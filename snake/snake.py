import pygame
import random
import sys

# Инициализация
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шарик-уклонист")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Игрок
player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# Препятствия
enemy_width = 40
enemy_height = 40
enemies = []
enemy_speed = 4
spawn_timer = 0

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Очки
score = 0

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed - player_radius > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed + player_radius < WIDTH:
        player_x += player_speed

    # Спавн врагов
    spawn_timer += 1
    if spawn_timer > 30:  # каждые 0.5 секунды
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemies.append([enemy_x, -enemy_height])
        spawn_timer = 0

    # Движение врагов
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Удаление врагов за экраном
    enemies = [e for e in enemies if e[1] < HEIGHT]

    # Проверка столкновений
    for enemy in enemies:
        dist_x = abs(player_x - (enemy[0] + enemy_width // 2))
        dist_y = abs(player_y - (enemy[1] + enemy_height // 2))
        if dist_x < player_radius + enemy_width / 2 and dist_y < player_radius + enemy_height / 2:
            running = False  # Конец игры

    # Рисуем игрока
    pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)

    # Рисуем врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Очки
    score += 1
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
