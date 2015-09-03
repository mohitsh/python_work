

class GameEntry:
	
	def __init__(self,name,score):
		self._name = name
		self._score = score
	
	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return '({0},{1})'.format(self._name,self._score)	


class Scoreboard:
	
	def __init__(self,capacity=10):
		self._board = [None]*capacity
		self._n = 0
	
	def __getitem__(self,k):
		return self._board[k]

	def __str__(self):
		return '\n'.join(str(self._board[j]) for j in range(self._n))
	
	def add(self,entry):
		score = entry.get_score()
