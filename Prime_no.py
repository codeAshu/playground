
#def prime_factors(n):
#"""Returns all the prime nos of a positive integer"""

    
def prime_list(start,end):
    factors = []
    factors.append(2)
    for i in range(start,end):
        d = 2
        while i > 1:
            while i % d == 0:
               i /= d
            d = d + 1
            if d*d > i:
                if i > 1: factors.append(i)
                break
    


    myset = set(factors)
    Prime_list = list(myset)
    Prime_list.sort()
    return factors   #gives all the prime nos in a perticular range

print prime_list(1,15)
