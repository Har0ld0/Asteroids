import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_split_movement = self.velocity.rotate(angle)
        second_split_movement = self.velocity.rotate(-angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        first_split = Asteroid(self.position.x, self.position.y, split_radius)
        second_split = Asteroid(self.position.x, self.position.y, split_radius)
        first_split.velocity = first_split_movement * 1.2
        second_split.velocity = second_split_movement * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
