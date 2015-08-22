

def libFine(actual,expected):
	ac_date = actual[0]
	ac_month = actual[1]
	ac_year = actual[2]

	ex_date = expected[0]
	ex_month = expected[1]
	ex_year = expected[2]

	if (ac_year < ex_year):
		return 0	
	elif (ac_year > ex_year):
		return 10000
	elif (ac_year == ex_year and ac_month > ex_month):
		return (ac_month-ex_month)*500
	elif (ac_year == ex_year and ac_month == ex_month):
		if (ac_date <= ex_date):
			return 0
		elif (ac_date > ex_date):
			return (ac_date-ex_date)*15
	elif (ac_year == ex_year and ac_month < ex_month):
		return 0

	

	#print ac_date
	#print ac_month
	#print ac_year
	#print ex_date
	#print ex_month
	#print ex_year

actual = raw_input().split()
actual = [int(x) for x in actual]
expected = raw_input().split()
expected = [int(x) for x in expected]
print libFine(actual,expected)

