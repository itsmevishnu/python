test  = int(input())

for i in range(test):
    a = list(raw_input())
    b = list(raw_input())
    total = len(a+b)
    common = len(set(a)-set(b))
    print(total-common)
