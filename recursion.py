# recursion.py
# Count down from a given number and store each step in an array
# Jackie P


def countdown(number):
	global number_list
	
	if number > 1:
		number_list.append(number)
		number -= 1
		countdown(number)
		
	else:
		print(number_list)
	

user_input = int(input("Enter number to start counting from: "))
number_list = []

countdown(user_input)

