from turtle import *
from tkinter import *
from construct import rewardRanking
from construct.createTurtles import gencolor
import time

def create(timeindex, tur, col):
	# Clear drawer's line and pen-it-up
	cv = getcanvas()
	screen = getscreen()
	Bgphoto = PhotoImage(file = "images/race/BGTurtleBlack.gif", master = cv)
	cv.create_image(-360, -300, image = Bgphoto, anchor = N+W)
	cv.image = Bgphoto
	clear ()
	pu ()
	# Clear turtles' lines
	for i in range (4):
		tur[timeindex[2 * i]].clear ()
	# Penup turtles
	for i in range (4):
		tur[timeindex[2 * i]].pu ()
	# Hide turtles
	for i in range (4):
		tur[timeindex[2 * i]].ht ()
	#Medals
	textID = cv.create_text(0, -180, text = "RECORD", font = ("Fipps",18,"italic"), fill = "#ffffff")
	# Draw the ranking
	ht ()
	y = 100
	setpos (-220, y)
	pd ()
	for i in range (3):
		forward (480)
		pu ()
		y -= 100
		goto (-220, y)
		pd ()
	pu ()
	x = -220
	setpos (x, 100)
	pd ()
	right (90)
	forward (200)
	for i in range (4):
		pu ()
		x += 120
		goto (x, 100)
		pd ()
		forward (200)
	# Write something :v
	pu ()
	goto (-280, 40)
	write ("Turtle", move=False, align="center", font=("Fipps", 15, "normal"))
	goto (-280, -60)
	write ("Time", move=False, align="center", font=("Fipps", 15, "normal"))
	# Turtle's rank
	x = -160
	for i in range (4):
		tur[timeindex[2 * i]].color(col[timeindex[2 * i]])
		tur[timeindex[2 * i]].goto (x, 50)
		tur[timeindex[2 * i]].left (90)
		x += 120
		tur[timeindex[2 * i]].st ()
	x = -165
	for i in range (4):
		goto (x, -55)
		x += 120
		write (("%0.2f" % timeindex[2 * i + 1]), move=False, align="center", font=("Arial", 10, "bold"))
	#Continue
	###Clear 2,3,4 turtle:
	time.sleep(3)
	cv.delete(textID)
	Bgphoto = PhotoImage(file = "images/race/BGTurtleBlack.gif", master = cv)
	cv.create_image(-360, -300, image = Bgphoto, anchor = N+W)
	cv.image = Bgphoto
	for i in range(1,4):
		tur[timeindex[i*2]].clear()
		tur[timeindex[i*2]].ht()
	clear()
	tur[timeindex[0]].right(90)
	tur[timeindex[0]].forward(165)
	tur[timeindex[0]].left(90)
	tur[timeindex[0]].backward(80)
	flag = 4
	temp = Turtle ()
	temp.penup ()
	temp.ht ()
	while(flag):
		for i in range(1,13):
			cv = getcanvas()
			dirImage = "images/reward_medals/F"
			dirImage = dirImage + str(i)
			dirImage = dirImage + ".png"
			Medal1 = PhotoImage(file = dirImage, master = cv)
			cv.create_image(-215, -150, image = Medal1, anchor = N+W)
			cv.image = Medal1
			Medal2 = PhotoImage(file = dirImage, master = cv)
			cv.create_image(-55, -190, image = Medal2, anchor = N+W)
			cv.image = Medal2
			Medal3 = PhotoImage(file = dirImage, master = cv)
			cv.create_image(105, -150, image = Medal3, anchor = N+W)
			cv.image = Medal3
			tur[timeindex[0]].forward(20)
			tur[timeindex[0]].backward(20)
			tur[timeindex[0]].color(gencolor())
			temp.speed(1)
			temp.forward(12)
		flag = flag - 1
