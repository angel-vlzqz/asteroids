import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while 1:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        dt = clock.tick(60) / 1000

        # update and draw
        updatable.update(dt)
        
        for asteroid in asteroids:
            asteroid.check_collision(player)

        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
