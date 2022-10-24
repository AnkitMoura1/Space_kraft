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


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(red_ship, (250, 200))
    WIN.blit(blue_ship, (650, 200))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
