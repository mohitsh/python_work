

def line_draw(n):
	print '-'*n

def eng_ruler(n):
	if n > 0:
		eng_ruler(n-1)
		line_draw(n)
		eng_ruler(n-1)

eng_ruler(5)
