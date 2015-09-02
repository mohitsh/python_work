

import os
def disk_usage(dudepath):
	total = os.path.getsize(dudepath)
	if os.path.isdir(dudepath):
		for child in os.listdir(dudepath):
			childpath = os.path.join(dudepath,child)
			total = total + disk_usage(childpath)
	return total

print disk_usage('/var/www')
