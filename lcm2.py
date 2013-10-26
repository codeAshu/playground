result = [1]

def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def union(a, b):
    """ return the union of two lists removing the duplicates"""
    return list(set(a) | set(b))

"""Returns the union of the factor with already existing numbers"""
def unionD(a,b):
    import collections
    a.sort()
    b.sort()
    d=union(a,b)
    
    c=[]
    ca=collections.Counter(a)
    cb=collections.Counter(b)
    i=0
    for i in range (0,len(d)):
        key = d[i]
        aVal = ca.get(key)
        bVal = cb.get(key)
        if(aVal >=bVal):
            while (aVal >0) :
                 c.append(key)
                 aVal = aVal-1
        else:
           while (bVal >0) :
               c.append(key)
               bVal = bVal-1
    return c

def minus(a, b):
    """ return the minus of two lists """
    return list(set(a) - set(b))


def factors(n):
    """Returns all the prime factors of a positive integer"""
    fact = []        
    d = 2
    while n > 1:
        while n % d == 0:
            fact.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: fact.append(n)
            break
    
    return fact

import time
ts = time.time()
no =[]
for i in range (0,19):
    no.append(i+1)

import Prime_no
pl = Prime_no.prime_list(1,20)

factorList = minus(no,pl)
#print factorList
for i in range (0, len(factorList)-1):
    f = factors(factorList[i])
    result = unionD(f,result)
    

result = unionD(result,pl)
print len result
lcm=1
for i in range (0,len(result)):
        lcm= lcm*result[i]

print lcm
print "run Time ="  +str( time.time() - ts)

    



    


