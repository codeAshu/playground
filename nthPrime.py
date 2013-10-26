def nthPrime(n):
    i=0
    m=3
    factors = set([2])
    Prime_list=[]
    while(len(factors) <n):
        d = 2
        i = m
        while i > 1:
            
            while i % d == 0:
                 i /= d
                 
            d = d + 1
            if d*d > i:
                if i > 1:factors.add(i)
        m=m+1

    
    return list(factors)
    
import time
ts = time.time()

print nthPrime(1001)
print "run Time ="+str( time.time() - ts)

    
