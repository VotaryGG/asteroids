import random

from circleshape import CircleShape
import pygame
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH




class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
       pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH) 

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        new_velocity_a = self.velocity.rotate(random_angle)
        new_velocity_b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = new_velocity_a * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = new_velocity_b * 1.2