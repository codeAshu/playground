def Prime(n):
    k=1
    while  (True):
        if( n<3):
            break
        
        elif ( ( n % 2 ) == 0) :
              n = n/2
              factors.append(2)

        elif ( ( n % 3 ) == 0) :
            n = n/3
            factors.append(3)

        elif ( ( n % (6*k -1) ) == 0) :
            n = n/(6*k -1)
            factors.append(6*k -1)
            k= k+1

        elif ( ( n % (6*k +1) ) == 0) :
            n= n/(6*k +1)
            factors.append(6*k +1)
            k= k+1

        
n= 78
factors = []
k=0
Prime(n)
print factors
print max(factors)

