letter = input()
if (letter >= 'a' and letter <='z') or (letter>='A' and letter<='Z'):
	if(letter in ['a','e','i','o','u','A','E','I','O','U']):
		print('Vowel')
	else:
		print('Consonant')
else:
	print('invalid')
