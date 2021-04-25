def largest( arr, n):
    largest = arr[0]
    for i in range(0,n):
        if largest<arr[i]:
            largest = arr[i]
    
    return largest

array = {1, 8, 7, 56, 90}
n = 5
print(largest(array,))