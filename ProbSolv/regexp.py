
import re
	
# pattern = re.search(pattern,str)

str = 'an example word:cat!!'

match = re.search(r'word:\w\w\w', str)

if match:
	print match.group()
else:
	print "no match"

match1 = re.search(r'iii', 'piiig')
if match1:
	print match1.group()

match2 = re.search(r'...it', 'shsjfshit')
if match2:
	print match2.group()

match3 = re.search(r'\d\d\d','mohit114')
if match3:
	print match3.group()

match4 = re.search(r'\w\w\w','!@#moh113')
if match4:
	print match4.group()

email = 'dabbakabba@somemail.com'
match5 = re.search(r'\w+@\w+.\w+',email)
if match5:
	print match5.group()

match6 = re.search('([\w.-]+)@([\w.-]+)\.([\w]+)', email)

if match6:
	print match6.group()	
	print match6.group(1)
	print match6.group(2)
	print match6.group(3)




