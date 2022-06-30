class Numbers:
    def __init__(self, n):
        self.n = n
        
    def generateNums(self):
        for i in range(self.n):
            yield i*i


num = Numbers(10)

gen = num.generateNums()

# for i in gen :
#     print(i)
# # print(gen)

print(gen.next())
