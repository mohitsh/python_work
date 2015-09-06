

import os
def disk_usage(dudepath):
	# total is the size of provided path
	total = os.path.getsize(dudepath)
	# check if path provided is a directory
	if os.path.isdir(dudepath):
	# for each child in path
		for child in os.listdir(dudepath):
		# make a path variable for child and add to total
			childpath = os.path.join(dudepath,child)
			total = total + disk_usage(childpath)
	return total

print disk_usage('/var/www')
