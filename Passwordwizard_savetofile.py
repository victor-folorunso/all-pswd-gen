import random
import sys

characters = []
	
#get all numbers to list
#for num in range(0,10):
#	characters.append(str(num))
		
#get all alphabets to list
#alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#for alphabet in alphabets:
#	characters.append((alphabet).lower())
#	characters.append((alphabet).upper())
		
#get all symbols to list
mixedspecial_characters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '\\', '|', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']
special_characters = []
		#cross check for error
for character in mixedspecial_characters:
	if character not in special_characters:
		special_characters.append(character)
		#append to main list
for character in special_characters:
	characters.append((character))
		
output_count = 1
length_pswd = 1#general password length
passwords = []
all_passwords = []
while output_count != 3:
	with open(f'output{output_count}.txt', 'w') as f:
		# Redirect standard output to the file
		sys.stdout = f
		
		#main loop
		while True:
			cache_pswd = []
			len_pswd_count = 0
			while len_pswd_count != length_pswd:
				cache_pswd.append(random.choice(characters))
				len_pswd_count += 1
			#make list become plain text(joined)
			result = ''.join(cache_pswd)
			#store password in list "passwords"
			if result not in passwords:
				#print(result)
				passwords.append(result)	
			if len(passwords) == pow(len(characters), length_pswd):#possible_combinations:
				#memory manager(3 lines removable)
				for password in passwords:
					all_passwords.append(password)
				passwords.clear()
				print(all_passwords)
				#output to file
				sys.stdout = sys.__stdout__
				#prepare for next iteration
				length_pswd += 1
				output_count += 1
				break

