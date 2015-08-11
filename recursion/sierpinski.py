
import turtle

def drawSierpinski(points,color,myTurtle):
	myTurtle.fillcolor(color)
	myTurtle.up()
	myTurtle.goto(points[0][0],points[0][1])
	myTurtle.down()
	myTurtle.begin_fill()
	myTurtle.goto(points[1][0],points[1][1])
	myTurtle.goto(points
