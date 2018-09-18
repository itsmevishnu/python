import random

def show_failure(random):

	print("""******************************\nYou are failed\n
The word is """+random + """\n
***********************""")
	exit()

#List of the words available
words = ["facebook", "twitter","whatsapp", "instagram","wordpress","youtube","google","yahoo"]

size = len(words)

# select the random item from the array
random_value = random.choice(words)

# print(random_value)
# remaining letters and chances
remaining = len(random_value)
total_tries = len(random_value)+10

while 1 :
	letter = raw_input("Enter letter\n")
	if len(letter)>1:
		print("Enter only one letter at a time\n")
	else:
		if letter in random_value:
			remaining -= random_value.count(letter)
			total_tries -= 1
			print("Remainig "+str(remaining)+" letters\n")
			print("Remainig "+str(total_tries)+"tries\n---------------------------------------")
			
			if remaining == 0 :
				print("**************************\nYou won the match\n**********************")
				exit()
			elif total_tries ==0:
				show_failure(random_value)
			else:
				continue
		else:
			total_tries -= 1
			print("Remainig "+str(remaining)+" letters\n")
			print("Remainig "+str(total_tries)+ "tries\n---------------------------------------")
			if total_tries ==0:
				show_failure(random_value)
			else:
				continue