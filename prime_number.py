# using Sieve Eratosthenes method
n = 50
prime = [ True for i in range(n)]

p = 2

while(p*p<n):
    if prime[p] == True:
        for i in range(p*p, n-1, p):
            prime[i] = False
    p +=1

for i in range(2, n):
    if prime[i]:
        print(i)