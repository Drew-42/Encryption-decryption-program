import random
import string

# A list of characters is made (blank space, letters, digits, other characters)

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# A unique key is constructed as a list of those characters, but randomly shuffled. The total 
# number of characters is so high that it's astronomically unlikely to get the same key twice

key = chars.copy()
random.shuffle(key)


# ENCRYPTION occurs here
plain_text = input('Enter a message to encrypt: ')
cipher_text = ''

for letter in plain_text:
	index = chars.index(letter)
	cipher_text += key[index]

print(f'Original message: {plain_text}')
print(f'Encrypted message: {cipher_text}')

print()

# DECRYPTION occurs here
cipher_text = input('Enter a message to decrypt: ')
plain_text = ''

for letter in cipher_text:
	index = key.index(letter)
	plain_text += chars[index]

print(f'Original message: {cipher_text}')
print(f'Decrypted message: {plain_text}')