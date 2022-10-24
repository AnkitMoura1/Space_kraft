import pygame
import os

WIDTH, HEIGHT = 900, 500
SHIP_H, SHIP_W = 55, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space kraft")
WHITE = (255, 255, 255)  # RGB
FPS = 60
BLACK = (0, 0, 0)
red_ship = pygame.image.load('Resources/redship.png')
red_ship = pygame.transform.scale(red_ship, (SHIP_W, SHIP_H))
blue_ship = pygame.image.load('Resources/blueship.png')
blue_ship = pygame.transform.scale(blue_ship, (SHIP_W, SHIP_H))
SPEED = 2
BORDER = pygame.Rect([WIDTH/2, 0, 10, HEIGHT])


def draw_window(red, blue):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(red_ship, (red.x, red.y))
    WIN.blit(blue_ship, (blue.x, blue.y))
    pygame.display.update()


def red_movement(red, keys_pressed):
    if keys_pressed[pygame.K_a] and red.x-SPEED > 0:  # red left
        red.x -= SPEED
    if keys_pressed[pygame.K_d] and red.x + SPEED < (WIDTH/2) - 40:  # red right
        red.x += SPEED
    if keys_pressed[pygame.K_w] and red.y - SPEED > 0:  # red up
        red.y -= SPEED
    if keys_pressed[pygame.K_s] and red.y + SPEED < HEIGHT-50:  # red down
        red.y += SPEED


def blue_movement(blue, keys_pressed):
    if keys_pressed[pygame.K_LEFT] and blue.x - SPEED > (WIDTH/2)+10:  # blue left
        blue.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and blue.x + SPEED < WIDTH-40:  # blue right
        blue.x += SPEED
    if keys_pressed[pygame.K_UP] and blue.y - SPEED > 0:  # blue up
        blue.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and blue.y + SPEED < HEIGHT-50:  # blue down
        blue.y += SPEED


def main():
    red = pygame.Rect([250, 200, SHIP_W, SHIP_H])
    blue = pygame.Rect([650, 200, SHIP_W, SHIP_H])
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(red, blue)
        keys_pressed = pygame.key.get_pressed()
        red_movement(red, keys_pressed)
        blue_movement(blue, keys_pressed)
    pygame.quit()


if __name__ == "__main__":
    main()
