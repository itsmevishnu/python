arr = [0,1,2,0,0,1,2,0,0,1,2]
lo = mid = 0
hi = len(arr) - 1

while( mid<=hi):
    if arr[mid] == 0:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        mid += 1
        lo += 1
    elif arr[mid] == 1:
        mid = mid+1
    else:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        hi = hi -1

print(arr)