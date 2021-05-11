array = [2, 3]
k = 4

n  =  len(array)

if(n<k):
    print("something wrong")
    exit()

total, max_sum = 0,0

# find the sum of initial values
for i in range(k):
    total += array[i]

max_sum = total  # assigning total to max_sum for comparing
for i in range(n-k):
    total = total - array[i] + array[i+k]
    max_sum = max(total, max_sum)
    
print(max_sum)