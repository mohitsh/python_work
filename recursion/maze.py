
class maze:
	def __init__(self, mazeFileName):
		rowsInMaze = 0
		colsInMaze = 0
		self.mazelist = []
		mazefile = open(mazeFileName, 'r')
		for line in mazefile:
			rowList = []
			col = 0
			for ch in line[:-1]:
				rowList.append(ch)
				if ch == "S":
					self.startRow = rowsInMaze
					self.startCol = col
				col = col + 1
			rowsInMaze = rowsInMaze + 1
			self.mazelist.append(rowList)
			columnsInMaze = len(rowList)
		
		self.rowsInMaze = rowsInMaze
		self.colsInMaze = colsInMaze
		self.xTranslate = -columnsInMaze/2
		self.yTranslate = rowsInMaze/2
		self.t = turtle.Turtle()
		self.wn  = turtle.Screen()
		#setup(width=800, height=800)
		self.wn.setworldcoordinates(-(colsInMaze-1)/2-.5,
					-(rowsInMaze-1)/2-.5,
					-(colsInMaze-1)/2+.5,
					-(rowsInMaze-1)/2+.5)
		
	def drawMaze(self):
		for y in range(self.rowsInMaze):
			for x in range(self.colsInMaze):
				if self.mazelist[y][x] == OBSTACLE:
					self.drawCenteredBox(x+self.xTranslate,
								-y+self.yTranslate,
									'tan')
		self.t.color('black','blue')
		self.t.fillcolor('blue')
		self.wn.update()
		self.wn.tracer(1)
	
	def drawCenteredBox(self,x,y,color):
		tracer(0)
		self.t.up()
		self.t.goto(x-.5,y-.5)
		self.t.color('black',color)
		self.t.setheading(90)
		self.t.down()
		self.t.begin_fill()
		for i in range(4):
			self.t.forward(1)
			self.t.right(90)
		self.t.end_fill()	
		#update()
		#tracer(1)
		
	def moveTurtle(self,x,y):
		self.t.up()	
		self.t.setheading(self.t.towards(x+self.xTranslate,
							-y+self.yTranslate))
		self.t.goto(x+self.xTranslate, -y+self.yTranslate)
		
	def dropBreadcrumb(self,color):
		self.t.dot(10,color)
	
	def updatePosition(self,row,col,val=None):
		if val:
			self.mazelist[row][col] = val
		self.moveTurtle(col,row)	
		
		if val == PART_OF_PATH:
			color = 'green'
		elif val == OBSTACLE:
			color = 'red'
		elif val ==  TRIED:
			color = 'black'
		elif val == DEAD_END:
			colot = 'red'
		else:
			color = None

		if color:
			self.dropBreadcrumb(color)


	def isExit(self,row,col):
		return (row == 0 or
			row == self.rowsInMaze -1 or
			col == 0 or 
			col == self.colsInMaze -1)

	def __getitem__(self,index):
		return self.mazelist[index]




def searchFrom(maze, startRow, startCol):
	maze.updatePosition(startRow, startCol)
	
	# is it a wall
	if maze[startRow][startCol] == OBSTACLE:
		return False
	
	# has it come back to same position
	elif maze[startRow][startCol] == TRIED:
		return False
	
	# has the turtle found an exit
	elif maze.isExit(startRow, startCol):
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
		return True
	
	maze.updatePosition(startRow, startCol, TRIED)
	
	found = searchFrom(maze, startRow-1, startCol) or  searchFrom(maze, startRow+1, startCol) or searchFrom(maze, startRow, startCol+1) or searchFrom(maze, startRow, startCol-1)

	if found:
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
	else:
		maze.updatePosition(startRow, startCol, DEAD_END)

	return found

 
import turtle

PART_OF_PATH = '0'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

myMaze = maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)












