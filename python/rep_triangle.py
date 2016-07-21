from turtle import *
def triangle(x, y, x1, y1, x2, y2, x3, y3):
	goto(x,y)
	pendown()
	goto(x1,y1)
	goto(x2,y2)
	goto(x,y)
	pencolor("SteelBlue4")
	begin_fill()
	goto(x3,y3)
	goto(x1, y1)
	end_fill()
	pencolor("black")
	penup()
	goto(x3,y3)
	pencolor("SteelBlue4")
	begin_fill()
	pendown()
	goto(x2,y2)
	end_fill()
	pencolor("black")
for i in range(8):
	triangle(0, 0, 120, 130, -120, 130, 0, 80)
	triangle(50,50,170,180,-70,180,50,130)
	triangle(100,100,220,230,-20,230,100,180)
	triangle(150,150,270,280,30,280,150,230)

	
