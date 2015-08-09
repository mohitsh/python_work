
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
	




def searchFrom(maze, startRow, startCol):
	maze.updatePosition(startRow, startCol)
	if maze[startRow][startCol] == OBSTACLE:
		return False
	elif maze[startRow][startCol] == TRIED:
		return False
	elif maze.isExit(startRow, startCol):
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
		return True
	maze.updatePosition(startRow, startCol, TRIED)
	
	found = searchFrom(maze, startRow-1, startCol) or 
		searchFrom(maze, startRow+1, startCol) or
		searchFrom(maze, startRow, startCol+1) or
		searchFrom(maze startRow, startCol-1)

	if found:
		maze.updatePosition(startRow, startCol, PART_OF_PATH)
	else:
		maze.updatePosition(startRow, startCol, DEAD_END)

	return found

 
