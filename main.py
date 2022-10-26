import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 500
SHIP_H, SHIP_W = 50, 40
BULLET_H, BULLET_W = 10, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space kraft")
WHITE = (255, 255, 255)  # RGB
FPS = 60
BLACK = (0, 0, 0)
red_ship = pygame.image.load('Resources/spaceship_red.png')
red_ship = pygame.transform.scale(red_ship, (SHIP_W, SHIP_H))
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)

# red_bullet = pygame.image.load('Resources/bullet.png')
# red_bullet = pygame.transform.scale(red_bullet, (BULLET_H, BULLET_W))

# blue_bullet = pygame.image.load("Resources/blue_bullet.png")
# blue_bullet = pygame.transform.scale(blue_bullet, (BULLET_W, BULLET_H))

blue_ship = pygame.image.load('Resources/spaceship_blue.png')
blue_ship = pygame.transform.scale(blue_ship, (SHIP_W, SHIP_H))

SPACE = pygame.image.load('Resources/space.png')
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

SPEED = 2
BORDER = pygame.Rect([WIDTH//2, 0, 10, HEIGHT])

red_bullets = []
blue_bullets = []
MAX_BULLETS = 3
BULLET_SPEED = 5

RED_HIT = pygame.USEREVENT + 1
BLUE_HIT = pygame.USEREVENT + 2
RED = (255, 0, 0)
BLUE = (0, 0, 255)


red_health = 10
blue_health = 10

WINNER_FONT = pygame.font.SysFont("comicsans", 100)


def draw_window(red, blue, r_bullet, b_bullet, b_hl, r_hl):
    WIN.fill(WHITE)
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render("Health: " + str(r_hl), True, WHITE)
    blue_health_text = HEALTH_FONT.render("Health: " + str(b_hl), True, WHITE)
    WIN.blit(red_health_text, (WIDTH-red_health_text.get_width() - 10, 10))
    WIN.blit(blue_health_text, (10, 10))
    WIN.blit(red_ship, (red.x, red.y))
    WIN.blit(blue_ship, (blue.x, blue.y))
    for bullet in r_bullet:
        # WIN.blit(red_bullet, (bullet.x, bullet.y))
        pygame.draw.rect(WIN, RED, [bullet.x, bullet.y, BULLET_W, BULLET_H])
    for bullet in b_bullet:
        # WIN.blit(blue_bullet, (bullet.x, bullet.y))
        pygame.draw.rect(WIN, BLUE, [bullet.x, bullet.y, BULLET_W, BULLET_H])
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


def handle_winner(text):
    draw_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,  HEIGHT//2 - draw_text.get_width()//2))
    pygame.display.update()
    pygame.time.delay(3000)


def handle_bullets(red_b, blue_b, red, blue):
    for bullet in red_b:
        bullet.x += BULLET_SPEED
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_b.remove(bullet)
        elif bullet.x > WIDTH:
            red_b.remove(bullet)

    for bullet in blue_b:
        bullet.x -= BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_b.remove(bullet)
        elif bullet.x < 0:
            blue_b.remove(bullet)


def main(red_hl, blue_hl):
    red = pygame.Rect([250, 200, SHIP_W, SHIP_H])
    blue = pygame.Rect([650, 200, SHIP_W, SHIP_H])
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    r_bullet = pygame.Rect([red.x+SHIP_W, red.y+(SHIP_H//2), BULLET_H, BULLET_W])
                    red_bullets.append(r_bullet)
                if event.key == pygame.K_RCTRL and len(blue_bullets) < MAX_BULLETS:
                    b_bullet = pygame.Rect([blue.x, blue.y + (SHIP_H // 2), BULLET_H, BULLET_W])
                    blue_bullets.append(b_bullet)

            if event.type == RED_HIT:
                red_hl -= 1

            if event.type == BLUE_HIT:
                blue_hl -= 1

        winner_text = None

        if red_hl <= 0:
            winner_text = "BLUE WINS"

        if blue_hl <= 0:
            winner_text = "RED WINS"

        if winner_text is not None:
            handle_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        red_movement(red, keys_pressed)
        blue_movement(blue, keys_pressed)
        handle_bullets(red_bullets, blue_bullets, red, blue)
        draw_window(red, blue, red_bullets, blue_bullets, red_hl, blue_hl)

    pygame.quit()


if __name__ == "__main__":
    main(red_health, blue_health)
