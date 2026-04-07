import sys
import pygame

WIDTH = 300
HEIGHT = 300
BG_COLOR = (25, 50, 90)
SNOWMAN_COLOR = (250, 250, 250)
EYE_COLOR = (20, 20, 20)
NOSE_COLOR = (255, 140, 0)
FPS = 60


def draw_snowman(surface):
    base_center = (WIDTH // 2, HEIGHT - 60)
    body_center = (WIDTH // 2, HEIGHT - 120)
    head_center = (WIDTH // 2, HEIGHT - 170)

    pygame.draw.circle(surface, SNOWMAN_COLOR, base_center, 40)
    pygame.draw.circle(surface, SNOWMAN_COLOR, body_center, 30)
    pygame.draw.circle(surface, SNOWMAN_COLOR, head_center, 22)

    pygame.draw.circle(surface, EYE_COLOR, (head_center[0] - 9, head_center[1] - 5), 4)
    pygame.draw.circle(surface, EYE_COLOR, (head_center[0] + 9, head_center[1] - 5), 4)

    pygame.draw.polygon(
        surface,
        NOSE_COLOR,
        [
            (head_center[0] + 14, head_center[1]),
            (head_center[0] + 28, head_center[1] + 4),
            (head_center[0] + 14, head_center[1] + 8),
        ],
    )


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lumememm - Metsjärv")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        draw_snowman(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
