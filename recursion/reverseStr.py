
def reverse(str):
	if len(str) == 1:
		return str[0]
	else:
		return str[len(str)-1] + reverse(str[:len(str)-1])

print reverse('tihom')
print reverse('aibohphobia')
print reverse('Live not on evil')
print reverse('kayak')
