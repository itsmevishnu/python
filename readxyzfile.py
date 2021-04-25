#Enter the xyz file path which you have to read
xyz=open('benzene.xyz')
#Reading all the lines in the xyz file
a = b =xyz.readlines()
xyz.close()
#counting the number of elements in the list 'a'
n = len(a)
#printing coordinates of all atoms
list1 = list2= []
for i in range(3,n-1):
    list1.append(a[i].split())
#iwthout split
# for i in range(3,n-1):
#     list2.append(b[i])

print("with split")
print(list1)

# print("Without split")
# print(list2)
    
