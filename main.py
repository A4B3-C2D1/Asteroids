import pygame
from constants import *

def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    black=(0,0,0)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()
        delta=clock.tick(60)
        dt=delta/1000


if __name__ == "__main__":
    main()