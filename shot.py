from circleshape import CircleShape
import pygame

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def check_collision(self, asteroid):
        return self.position.distance_to(asteroid.position) < self.radius + asteroid.radius
