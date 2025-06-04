# big 'ol rocks
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velo1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        velo2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radii)
        ast2 = Asteroid(self.position.x, self.position.y, new_radii) 
        ast1.velocity = velo1 * 1.2
        ast2.velocity = velo2 * 1.2