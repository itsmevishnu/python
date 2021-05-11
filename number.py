n =  int(input("Enter any number"))

sum = 0
position = 1

while(n):
    rem = n%10
    if(rem==0):
        sum = sum + position * 5
    else:
        sum = sum +  position * rem
    
    n = n//10
    position = position * 10

print("Number after edit", sum)