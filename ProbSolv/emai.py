
import re
def emailcheck(email):
	if "@" in email:
		ind1 = email.index('@')
		name = email[:ind1]
		fname = re.search("[^A-Za-z0-9_-]+", name)
		if not name:
			return None
		if "." in email:
			ind2 = email.index(".")
			host = email[ind1+1:ind2]
			ext = email[ind2+1:]
			fweb = re.search("[^A-Za-z0-9]+",host)
			if not host or not ext:
				return None

			if not fname and not fweb and len(ext) < 4:
				return email
			else:
				return None
	else:
		return None


n = int(raw_input())
arr = []
for i in range(n):
	email = raw_input()
	arr.append(str(email))

arr  = list(filter(lambda x: emailcheck(x), arr))
arr.sort()
print arr


