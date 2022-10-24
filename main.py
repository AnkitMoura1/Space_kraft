import pygame
import os

WIDTH, HEIGHT = 900, 500
SHIP_H, SHIP_W = 55, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space kraft")
WHITE = (255, 255, 255)  # RGB
FPS = 60
red_ship = pygame.image.load('Resources/redship.png')
red_ship = pygame.transform.scale(red_ship, (SHIP_W, SHIP_H))
blue_ship = pygame.image.load('Resources/blueship.png')
blue_ship = pygame.transform.scale(blue_ship, (SHIP_W, SHIP_H))
SPEED = 1


def draw_window(red, blue):
    WIN.fill(WHITE)
    WIN.blit(red_ship, (red.x, red.y))
    WIN.blit(blue_ship, (blue.x, blue.y))
    pygame.display.update()


def red_movement(red, keys_pressed):
    if keys_pressed[pygame.K_a]:  # red left
        red.x -= 1 + SPEED
    if keys_pressed[pygame.K_d]:  # red right
        red.x += 1 + SPEED
    if keys_pressed[pygame.K_w]:  # red up
        red.y -= 1 + SPEED
    if keys_pressed[pygame.K_s]:  # red down
        red.y += 1 + SPEED


def blue_movement(blue, keys_pressed):
    if keys_pressed[pygame.K_LEFT]:  # blue left
        blue.x -= 1 + SPEED
    if keys_pressed[pygame.K_RIGHT]:  # blue right
        blue.x += 1 + SPEED
    if keys_pressed[pygame.K_UP]:  # blue up
        blue.y -= 1 + SPEED
    if keys_pressed[pygame.K_DOWN]:  # blue down
        blue.y += 1 + SPEED


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
