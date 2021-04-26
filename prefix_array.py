array = [1,2,3,4,5]
prefixarray = [0 for i in range(0,5)]

prefixarray[0] =  array[0]

for i in range(1,len(array)):
    prefixarray[i] = prefixarray[i-1]+array[i]


print(prefixarray)