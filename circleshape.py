import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collision(self, theother):
        #theother ist einfach nur der andere, name wird nachher angepasst
        distance =self.position.distance_to(theother.position) #(asteroid 1 durch self und der andere in der klammer)
        sum_of_radii = self.radius + theother.radius
        return distance <= sum_of_radii
# wenn die distance zwischen den beiden asteroiden kleiner ist als die beiden radii zusammen dann kollidieren die asteroiden

