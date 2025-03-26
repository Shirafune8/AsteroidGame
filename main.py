import pygame
from constants import *
from player import *

def main():
#start game
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() # create Clock object before game loop
    dt = 0 # delta time
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Game loop using While loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        player.draw(screen)   
        player.update(dt) 
        pygame.display.flip()

        dt = clock.tick(60) / 1000 #convert ms to sec

# no need to touch below
if __name__ == "__main__":
    main()