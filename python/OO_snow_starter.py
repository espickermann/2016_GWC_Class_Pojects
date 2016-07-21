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
GREY = (176,196,222)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (	0,191,255)
BLUE = (224,255,255)
ORANGE = (255,99,71)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    #gives charachteristics
    def __init__(self, size, position, wind=False):
        self.size = size
        self.position = position
        self.wind = wind		
    
    
    #uses the charachteristics
    def fall(self, speed):
        """
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        """
        self.position[1] += speed
        if self.wind == True:
            self.position[0] += speed//2
    def draw(self):
        """
        Uses pygame and the global screen variable to draw the snowflake on the screen
        """
        global WHITE
        global GREY
        global BLUE
        global RED
        color = random.randint(0,3)
        color_list = [RED, GREY, BLUE, WHITE]
        
        global screen
        pygame.draw.circle(screen, color_list[color], self.position, self.size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = 10


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []
for i in range(10000):
    snow_list.append(SnowFlake(random.randint(5,10), [random.randint(10,700), random.randint(0,50)], wind= False))
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    background = pygame.image.load('yosemitewinter.jpg')
    screen.blit(background, [0,0])

    # --- Drawing code should go here
    # Begin Snow

    z=0
    for i in snow_list:
        snow_list[z].draw()
        snow_list[z].fall(random.randint(5,60))
        z +=1


    pygame.draw.circle(screen, WHITE, (10,450), 100)
    pygame.draw.circle(screen, WHITE, (10,350), 70)
    pygame.draw.circle(screen, WHITE, (10,250), 50)
    pygame.draw.rect(screen, BLACK, (25,240,10,10), 5)
    pygame.draw.lines(screen, ORANGE, True, [(60,250), (65,255), (60,260)], 5)
	
    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    for i in range(random.randint(2,9)):
        snow_list.append(SnowFlake(random.randint(5,10), [random.randint(10,700), random.randint(0,50)], wind= True))
    # --- Limit to 60 frames per second
    clock.tick(90)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
