import asyncio
import sys

import pygame

COLORS = ('yellow', 'blue', 'red')
FPS = 25


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            current_row = 0
            current_color = 0

            if event.key == pygame.K_w:
                current_row = (current_row - 1) % len(COLORS)
                new_color = COLORS[current_row]
                screen.fill(new_color)
                pygame.display.update()
            elif event.key == pygame.K_s:
                current_row = (current_row + 1) % len(COLORS)
                new_color = COLORS[current_row]
                screen.fill(new_color)
                pygame.display.update()
            elif event.key == pygame.K_a:
                current_color = (current_color - 1) % len(COLORS[current_row])
                new_color = COLORS[current_color]
                screen.fill(new_color)
                pygame.display.update()
            elif event.key == pygame.K_d:
                current_color = (current_color + 1) % len(COLORS[current_row])
                new_color = COLORS[current_color]
                screen.fill(new_color)
                pygame.display.update()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())

print('For add commit')
