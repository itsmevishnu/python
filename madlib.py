print ("Lets play mad lib game?\n")

def game_structure():
	# reading exclamation
	exclamation = raw_input("Enter an exclamation word\n")

	# reading adverb
	adverb = raw_input("Enter an adverb word\n")

	# reading noun
	noun = raw_input("Enter a noun as you like\n")

	# reading adejctive
	adjective = raw_input("Enter an adjective\n")

	# create the story

	story = exclamation.capitalize() + "!, he said " + adverb +" as he jumped into his convertible "+ noun + " and drove off with his "+adjective+" wife."

	# print the story
	print("The story \n******************")
	print("\n"+story) 
	print("******************************************\n")

	option = raw_input("Do you want to play again? Y/N\n")
	return option

option = game_structure()

if option=="y" or option =="Y":
	game_structure()
elif option=="n" or option=="N":
	exit()
else:
	print("You are entered a wrong keyword, Game terminates")