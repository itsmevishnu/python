import random

gamelist = {1: "rock",2:"scissors",3:"paper"}

comp = random.radomint(gamelist)

print("Rock-Paper-Scissor game\n*********************\n")

for i in range(len(gamelist)):
	print(str(i+1) +" : " + gamelist[i] )

my_choice = input("Enter your option\n")

