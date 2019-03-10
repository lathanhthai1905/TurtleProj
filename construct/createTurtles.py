from turtle import *
from random import randint


#Generate colours of turtles
def gencolor():
	r = lambda: randint(0, 255)
	return ('#%02X%02X%02X' % (r(), r(), r()))


#Create turtles absolutely
def create(n):
	#Set the default coordinates
	if (n == 13):
		x, y, spin = -130, 0, 0
	elif (n == 17):
		x, y, spin = -170, 0, 0
	elif (n == 21):
		x, y, spin = -210, 0, 0

	tur = []
	color = []

	for n in (gencolor(),gencolor(),gencolor(),gencolor()):	  #Create the turtles
	#Customize the turtles
		t = Turtle()
		# bluebear = "images/characters/set1/Bluebearforward.gif"
		register_shape("banhmy", ((-4,3),(-4,1),(-2,2),(0,4),(2,2),(4,3),(4,1),(2,2),(0,-2),(-1,-3),(1,-3),(-2,2)))
		t.color(n)
		t.shape("banhmy")
		t.shapesize(3, 3, 1)

	#Move turtles to the start point
		t.penup()
		t.goto(x,y)
		t.pendown()
		y -= 30

	#Spin each turtle
		spin += 1
		if (spin % 2 == 0):
			t.right(360)
		else:
			t.left(360)

		tur.append(t)
		color.append(n)

	return tur,color	#Return the list of turtles
