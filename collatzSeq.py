"""run Time = 31.6692640781"""

def getSeq(n):
    possible_long = range(0,n)
    confirmed_long =[]
    inc = 2   
    while(inc<n):
         possible_long[inc] = False
         inc = inc+2

    for i in range (2,n):
        if possible_long[i] !=False:
            confirmed_long.append(possible_long[i] )
    return confirmed_long

def collatz(n):
    i=1
    #print n
    while(True):
        if n%2 == 0:
            n = n/2
            #print n
            i+=1
        else:
            n=3*n+1
            #print  n
            i+=1
        if n==1:
            return i
        
import time
ts = time.time()

cl= getSeq(1000000)
maxm =1
num=0
for i in cl :
    length = collatz(i)
    if length>maxm:
        maxm = length
        num = i

print num
print maxm
print "run Time =", time.time() - ts

        
