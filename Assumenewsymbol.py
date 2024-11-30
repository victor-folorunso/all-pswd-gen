import random

#assumimg a new symbol (¿)was discovered
all_passwords = ['achju']#this is all generated psswords
new_characters = ['¿']#this is all the new symbols


for selected in new_characters:
	for password in all_passwords:
		characters = []
		for character in password:
			characters.append(character)
		characters.append(selected)
		print(characters)
		print("please wait,processing huge data....")
		
		length_pswd = len(characters) #general password length
		passwords = []
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
				passwords.append(result)	
			if len(passwords) == pow(len(characters), length_pswd) :#possible_combinations:
				print(f"{passwords}\n")
				break
#it returns a list or each new password combined with each new character
#since the "all_password major"  list is unsorted,i guess these should just be stacked untop
		
		
		
			