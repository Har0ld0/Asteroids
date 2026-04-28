import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
