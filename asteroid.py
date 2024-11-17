from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "green",  radius=self.radius, center=self.position, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        self.spawn_debris()
    
    def spawn_debris(self):
        import random
        angle=random.uniform(20,50)
        dir1=self.velocity.rotate(angle)
        dir2=self.velocity.rotate(-angle)
        new_radius=self.radius- ASTEROID_MIN_RADIUS
        debris1=Asteroid(*self.position, new_radius)
        debris2=Asteroid(*self.position, new_radius)
        debris1.velocity=dir1
        debris2.velocity=dir2