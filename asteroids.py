from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            velocity_a = self.velocity.rotate(angle)
            velocity_b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = velocity_a * 1.2

            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity = velocity_b * 1.2