import pygame
from constants import *
from player import *
from circleshape import *
from asteroids import *
from asteroidfield import * 
from shots import *

def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    black=(0,0,0)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shots.containers = (updatable,drawable,shots)
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        for updates in updatable:
            updates.update(dt)
        for asteroid in asteroids:
            if(player.collision(asteroid)==True):
                raise SystemExit("Game over!")
            for shot in shots:
                if(shot.collision(asteroid)==True):
                    asteroid.split()
                    shot.kill()

        for draws in drawable:
            draws.draw(screen)
        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()
        delta=clock.tick(60)
        dt=delta/1000


if __name__ == "__main__":
    main()