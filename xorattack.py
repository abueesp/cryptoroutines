string = raw('Insert hexadecimal string')
message = raw('Enter known message')
tocipher = raw('Now you will get the key. Introduce the text to encrypt')

def strxor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

print strxor(strxor(string.decode('hex'), message), tocipher).encode('hex')
