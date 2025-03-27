import pygame
import random
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
#start game
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock() # create Clock object before game loop
    dt = 0 # delta time

    #create groups before you create any instances so that those instances can be immediately grouped
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()
    
    # Assign groups to Player and Asteroid class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (all_shots, updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) #build last

    # Game loop using While loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 # limit framerate to 60 FPS and convert ms to sec
    
        updatable.update(dt)  # Updates all sprites in the "updatable" group
        
        screen.fill((0,0,0)) # creates screen colour

        for sprite in drawable:
            sprite.draw(screen)  # You must call `draw()` for each drawable sprite
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()

        for asteroid in all_asteroids: # check if an asteroid hits the player
            if asteroid.collision_check(player):
                print("Game Over!")
                exit()
            for bullet in all_shots: #check if asteroid collides with bullet
                if asteroid.collision_check(bullet):
                    asteroid.split() # remove the asteroid
                    bullet.kill() # remove the bullet

        pygame.display.flip()

# no need to touch belowa
if __name__ == "__main__":
    main()