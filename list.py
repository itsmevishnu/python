my_list = []

for i in range(0,10,1):
	number = input("Enter the "+ str(i+1) + "position number" )
	my_list.append(number)
print("**************************")
print("The numbers less than 10\n")
for i in my_list:
	if( i< 10):
		print(i)