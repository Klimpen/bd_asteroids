# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid and asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if shot and asteroid and asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()