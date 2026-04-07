import sys
import pygame

WIDTH = 800
HEIGHT = 600
BG_COLOR = (30, 30, 30)
SQUARE_COLOR = (255, 200, 0)
SQUARE_SIZE = 50
SPEED = 5


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ruut")
    clock = pygame.time.Clock()

    x = (WIDTH - SQUARE_SIZE) // 2
    y = (HEIGHT - SQUARE_SIZE) // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= SPEED
        if keys[pygame.K_RIGHT]:
            x += SPEED
        if keys[pygame.K_UP]:
            y -= SPEED
        if keys[pygame.K_DOWN]:
            y += SPEED

        x = max(0, min(WIDTH - SQUARE_SIZE, x))
        y = max(0, min(HEIGHT - SQUARE_SIZE, y))

        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, SQUARE_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
