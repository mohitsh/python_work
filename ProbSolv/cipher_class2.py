
class Cipher:
	def __init__(self,shift):
		encoder = [None]*26
		decoder = [None]*26
		
		for k in range(26):
			encoder[k] = chr((k+shift)%26 + ord('A'))
			decoder[k] = chr((k-shift)%26 + ord('A'))

		self._forward = ''.join(encoder)
		self._backward = ''.join(decoder)
	
	def encrypt(self,message):
		return self._transform(message,self._forward)

	def decrypt(self,secret):
		return self._transform(secret,self._backward)

	def _transform(self,msg,code):
		alist = list(msg)
		for i in range(len(alist)):
			if alist[i].isupper():
				index = ord(alist[i])-ord('A')
				alist[i] = code[index]
		return ''.join(alist)


if __name__ =='__main__':
	cipher = Cipher(10)
	message = 'THEY KNOW THE STRATEGY ABORTH THE MISSION! ABORT THE MISSION'
	coded = cipher.encrypt(message)
	print 'incrypted -->',coded
	decoded = cipher.decrypt(coded)
	print 'decrypted -->',decoded
	
	
