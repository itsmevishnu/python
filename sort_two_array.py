
# list1 = [2,3,4,5] - input
# list2 = [4,2,8,10] -Input
# final_array = [2,3,4,5,4,2,8,10] = intermediate result
# sorted_array = [2,2,3,4,4,5,8,10] == Output

def sort_array(input, length):
    i = 0
    while(i < length - 1):
        if(input[i] > input[i+1]):
            input[i], input[i+1] = input[i+1], input[i]
            i = -1
        i = i+1
    return input

list_1 = [2,3,4,5]
list_2 = [4,2,8,10]


final_array = list_1+list_2

sorted_array = sort_array(final_array, len(final_array))

print(sorted_array)

