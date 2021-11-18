

def alt_case(input_string):
	for i in range(len(input_string)):
		if len(input_string) % 2 == 0:
			if i % 2 == 0:
				input_string[i] = input_string[i].upper()
			else:
				input_string[i] = input_string[i].lower()
		else:
			if i % 2 == 0:
				input_string[i] = input_string[i].lower()
			else:
				input_string[i] = input_string[i].upper()
	return(input_string)

#def i in range length string, if i even upper, if i odd lower

input_string = list(input("put in smth: "))
alt_case(input_string)
print(str(input_string))