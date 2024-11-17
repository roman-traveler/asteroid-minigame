# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    clock, dt = pygame.time.Clock(), 0
    player=Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return
        for item in updatable:
            item.update(dt)
        screen.fill("#000000")
        for item in drawable:
            item.draw(screen) 
        pygame.display.flip()
        dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()
