import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


#hier wird der gameloop abgespielt und geupdated

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid): #check ob eine collision passiert
                print("Game Over!")
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    print("Collision detected!")
                    shot.kill()
                    asteroid.split()
                    
        
        

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        screen.fill("black")
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()