# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    clock, dt = pygame.time.Clock(), 0
    player=Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    ast_field=AsteroidField()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collide(bullet):
                    bullet.kill()
                    asteroid.split()
            if asteroid.collide(player):
                print("Game Over!")
                return
        screen.fill("#000000")
        for item in drawable:
            item.draw(screen) 
        pygame.display.flip()

        dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()
