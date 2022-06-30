def square(n):
    return n*n

nums = [x for x in range(10)]

squares = map(square,nums)

print(list(squares))