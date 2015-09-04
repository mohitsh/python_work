


class CaesarCipher:
	
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

	def _transform(self,original,code):
		msg = list(original)
		for i in range(len(msg)):
			if msg[i].isupper():
				index = ord(msg[i]) - ord('A')
				msg[i] = code[index]
		return ''.join(msg)

if __name__ == '__main__':
	cipher = CaesarCipher(3)
	message = "THE EAGLE IS IN PLAY; MEET AT JOI'S"
	coded = cipher.encrypt(message)
	print ('Secret: ',coded)
	answer = cipher.decrypt(coded)
	print ('Message: ',answer)