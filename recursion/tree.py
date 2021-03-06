
import turtle
t = turtle.Turtle()
end = turtle.Screen()

def tree(branchLen, t):
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		tree(branchLen-10,t)
		t.left(40)
		tree(branchLen-10,t)
		t.right(20)
		t.backward(branchLen)
	

t.left(90)
t.up()
t.backward(100)
t.down()
t.color('blue')
tree(75,t)
end.exitonclick()
