
def sierpinski(points, degree, myTurtle):
	colormap = ['blue','red','orange','green','white','pink',
			'yellow', 'violet']
	drawTriangle(points ,colormap[degree], myTurtle)
	if degree > 0:
		sierpinski([points[0],
				getmid(points[0], points[1]),
				getmid(points[0], points[2])],
				degree - 1, myTurtle)
		sierpinski([points[1], 
				getmid(points[1], points[0]),
				getmid(points[1], points[2])],
				degree - 1, myTurtle)
		sierpinski([points[2],
				getmid(points[2], points[0]),
				getmid(points[2], points[1])],
				degree - 1, myTurtle)

def getmid(pt1, pt2):
	return ((pt1[0] + pt2[0])/2, (pt1[1] + pt2[1])/2)


import turtle
def drawTriangle(points, color, myTurtle):
	myTurtle.fillcolor(color)
	myTurtle.up()
	myTurtle.goto(points[0][0], points[0][1])
	myTurtle.down()
	myTurtle.begin_fill()
	myTurtle.goto(points[1][0],points[1][1])
	myTurtle.goto(points[2][0],points[2][1])
	myTurtle.goto(points[0][0],points[0][1])
	myTurtle.end_fill()

def main():
	myTurtle = turtle.Turtle()
	myWin = turtle.Screen()
	myPoints = [[-100,-50],[0,100],[100,-50]]
	sierpinski(myPoints,3,myTurtle)
	myWin.exitonclick()

main()

	
