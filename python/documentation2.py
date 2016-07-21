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

circle_list = []


class Circle():
	def __init__(self, mouse_position):
		self.mouse_position = mouse_position
		self.x = mouse_position[0]
		self.y = mouse_position[1]
	def draw(self):
		global screen
		global RED
		x = self.x
		y = self.y
		pygame.draw.circle(screen, RED, (x, y), 20)
	def move(self):
		global screen
		global RED
		x = self.x
		y = self.y
		x += 70
		y += 70
		pygame.draw.circle(screen, RED, (x, y), 20)
screen.fill(WHITE)
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		

	
	mouse_position = pygame.mouse.get_pos()	
	pressed = pygame.mouse.get_pressed()


	circ1 = Circle(mouse_position)
	if 	pressed[0] == 1:
		print("here")

		circle_list.append(circ1)
		circ1.draw()
		

	while not done:
		circ1.move()

			
	# for i in circle_list:
		# z = 0
		# circle_list[z].move()
		# z +=1
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()
exit()
		