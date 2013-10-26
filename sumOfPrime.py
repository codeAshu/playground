def SumPrime(n):
    prime = set([2])
    for i in range(0,n):
        d = 2
        while i > 1:
            
            while i % d == 0:
                 i /= d
                 
            d = d + 1
            if d*d > i:
                if i > 1:prime.add(i)
                break

    #print list(prime)
    return sum(list(prime))

import time
ts = time.time()

print "sum of all prime  ", SumPrime(10)
print "run Time =", time.time() - ts
