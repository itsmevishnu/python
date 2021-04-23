#array package is used to create array datastrcutre in Python
import array;

'''array function is used to create array. 
First Parameter is type of the array, 
second parameter is array elements
i - integer
b- character
f-float
d -double
'''

array1= array.array('i', [1,2,3])
# print the array1
print("Array")
for i in array1:
    print(i)

# append function is used to add one element to the array
array1.append(5)
# Print new array
print("Array after append new value\n")
for i in array1:
    print(i)

''' Insert function is used to insert into the array
first parameter is the location in which we wanted to insert
secind parameter is the value need to insert'''
array1.insert(3,4)
print("Array after insert\n")
for i in array1:
    print(i)