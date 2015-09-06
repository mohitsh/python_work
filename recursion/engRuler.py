

def draw_line(tick_length):
	line  = '-'*tick_length
	print line, tick_length

def draw_interval(center_length):
	if center_length > 0:
		draw_interval(center_length-1)
		draw_line(center_length)
		draw_interval(center_length-1)
	

draw_interval(5)
