

# we have three towers From, Via and To
# From: initial tower
# Via: intermediate tower
# To: final tower

# this function attempts to move a tower of height h
# from From tower to To tower
def moveTower(h,From,Via,To):
	
	if h >= 1:
		# move tower of height (n-1) i.e. tower 
		# leaving the bottom disk to Via tower through
		# tower To
		moveTower(h-1, From, To, Via)
		# at this stage only last disk is left on the 
		# From pole. Move that disk to To pole
		moveDisk(From, To)	
		# Now rest of the tower i.e. height of (h-1)
		# is on Via tower. Shift this tower to To through From
		moveTower(h-1,Via,From,To)

	
def moveDisk(From, To):
	print 'moving disk from ', From, ' to ', To

moveTower(3,'A','B','C')

