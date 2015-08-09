
import turtle

# playground for turtle
playground = turtle.Screen()
playground.bgcolor('lightgreen')
playground.title('Jain and Mittal Turtle')

# jain is my turtle
jain = turtle.Turtle()

jain.color('blue')
jain.pensize('3')
jain.shape('blank')

# a rectangle
for i in range(4):
	jain.forward(100)  # initial direction in east
	jain.left(90)     # so array goes in right direction when forward
	


mittal = turtle.Turtle()
mittal.color('hotpink')
mittal.pensize(4)
mittal.shape('arrow')

# a rectangle
for i in range(4):
	mittal.forward(100)
	mittal.right(90)

bhai = turtle.Turtle()
bhai.color('black')
bhai.pensize(2)
bhai.shape('turtle')
bhai.speed(2)

# a triangle
bhai.right(300)
for i in range(3):
	bhai.stamp()
	bhai.forward(120)
	bhai.right(120)


playground.exitonclick()
