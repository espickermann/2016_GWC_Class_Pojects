import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)


screen.fill(WHITE)

class Circle():
	def __init__(self, mouse__position):
		self.mouse_position = mouse_position
	def draw(self):
		pygame.draw.circle(screen, RED, mouse_position, 20)
	
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
	
	
	mouse_position = pygame.mouse.get_pos()	
	pressed = pygame.mouse.get_pressed()
	if 	pressed[0] == 1:
		print("here")
		pygame.draw.circle(screen, RED, mouse_position, 20)	
		
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()
exit()
		