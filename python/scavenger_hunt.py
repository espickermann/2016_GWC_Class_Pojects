"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
DarkSeaGreen3 = (100, 250, 200)

color_list = [BLACK, WHITE, GREEN, RED, BLUE, GREY, DarkSeaGreen3]

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x = 350
y = 250

direction = 1

direction1 = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    top = y
    bottom = y
    left = x
    right = x
    randomcolor = color_list[random.randint(0,len(color_list)-1)]

    # --- Game logic should go here
  
    if right > 699:
        x -=5
        direction = 1
    elif left < 1:
        x +=5
        direction = -1
    elif direction > 0:
        x -=5
    elif direction < 0:
	    x +=5
    if top < 0:
        y +=5
        direction1 = 1
    elif bottom > 500:
        y -=5
        direction1 = -1
    elif direction1 > 0:
        y +=5
    elif direction1 < 0:
	    y -=5
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    screen.fill(DarkSeaGreen3)
    # --- Drawing code should go here
    pygame.draw.circle(screen, randomcolor, (x,y), 30, 10)
    ball = pygame.draw.circle(screen, randomcolor, (x,y), 30, 10)
 

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
