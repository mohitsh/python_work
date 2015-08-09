
import turtle

dobby = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(dobby, lineLen):
	if lineLen > 0:
		dobby.forward(lineLen)
		dobby.right(90)
		drawSpiral(dobby, lineLen-5)
	
drawSpiral(dobby, 50)
myWin.exitonclick()
