import asyncio
import pygame
import sys

COLORS = [
    [(128, 0, 128), (255, 0, 0), (0, 0, 255)],  # purple, red, blue
    [(255, 255, 255), (255, 255, 0), (0, 128, 0)],  # white, yellow, green
]
FPS = 40


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    current_row = 0
    current_color = 0


    while True:
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_w:
                current_row = (current_row - 1) % len(COLORS)
            elif event.key == pygame.K_s:
                current_row = (current_row + 1) % len(COLORS)
            elif event.key == pygame.K_a:
                current_color = (current_color - 1) % len(COLORS[current_row])
            elif event.key == pygame.K_d:
                current_color = (current_color + 1) % len(COLORS[current_row])
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


            new_color = COLORS[current_row][current_color]
            screen.fill(pygame.Color(new_color))
            pygame.display.update()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
