energy_file = open('output.out','r')
content = energy_file.readlines()
values_array = []
for i in range(432, 452):
    values_array.append(content[i].split())

print(values_array)