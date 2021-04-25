#find the sum divisible by 9, from 50 to 100
n = 100
sum  = 0
for i in range(50, n): 
    if(i % 9 == 0): 
        print (i)
        sum = sum+i

print(sum)