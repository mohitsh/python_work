
import re
def emailcheck(email):
	ind1 = email.index("@")
	ind2 = email.index(".")

	name = email[:ind1]
	website = email[ind1:ind2]
	ext =  email[ind2:]
	
	if re.match("^[A-Za-z0-9_-]*$", name) and re.match("^[A-Za-z0-9]*$", website) and len(ext) <= 3:
		print "correct!"


email  = str(raw_input())

emailcheck(email)

