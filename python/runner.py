import pygame
import random

from city_2 import Scroller
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



a=0
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)
#defining stuff for scroller scroller class used in while loop 

back_scroller = Scroller(screen, SCREEN_WIDTH, 100, SCREEN_HEIGHT-100, BACK_SCROLLER_COLOR, 1)
middle_scroller = Scroller(screen, SCREEN_WIDTH, 300, SCREEN_HEIGHT-70, MIDDLE_SCROLLER_COLOR, 2)
front_scroller = Scroller(screen, SCREEN_WIDTH, 500, SCREEN_HEIGHT-20, FRONT_SCROLLER_COLOR, 3)

class runner_sprite(pygame.sprite.Sprite):
	def __init__ (self):
		pygame.sprite.Sprite.__init__ (self) 
		self.image = pygame.image.load("bird.png")
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (60,60))
	def draw(self, pos):	   
		global screen
		screen.blit(self.image, pos)
		self.rect.move(x, y) #moves the rect
	def stay(self):
		screen.blit(self.image, ?????)
		
#player sprite stuff

bird = runner_sprite()
idk = runner_sprite()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(bird)

while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

			
			
	if a%30==0:
		back_scroller.add_building(-100)
	if a%20==0:
		middle_scroller.add_building(-100)
	if a%10==0:
		front_scroller.add_building(-100)
	a+=1		
			
			
	screen.fill(BACKGROUND_COLOR)			
			
			
	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()	
	
	x = pygame.mouse.get_pos()[0]-30 
	y = pygame.mouse.get_pos()[1]-30
	bird.draw((x, y))
	idk.stay() #do stuff with this 
	
	# charachter.image()
# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
# exit() # Needed when using IDLE