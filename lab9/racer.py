import pygame
import random

white = (255, 255, 255)
eraser = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Игровые параметры
radius = 15
mode = white
last_pos = None
coins_collected = 0
enemy_speed = 5

coins = []

def drawLineBetween(screen, start, end, width, color_mode):
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def drawCoin(screen, pos, color):
    pygame.draw.circle(screen, color, pos, 10)

def generate_coin():
    x = random.randint(20, 620)
    y = random.randint(20, 460)
    weight = random.randint(1, 3)  # случайный вес
    return (x, y, weight)

# Главная функция
def main():
    global coins_collected, enemy_speed

    while True:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:
                    mode = eraser
                elif event.key == pygame.K_w:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)

       
        if random.random() < 0.02:  # 2% шанс на генерацию монеты
            coin = generate_coin()
            coins.append(coin)


        for coin in coins:
            drawCoin(screen, (coin[0], coin[1]), yellow)

        # Двигаем врага, увеличиваем скорость при сборе монет
        if coins_collected >= 5:
            enemy_speed = 10  # Увеличение скорости врага

    
        font = pygame.font.SysFont("arial", 20)
        text = font.render(f"Coins Collected: {coins_collected}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)


main()
