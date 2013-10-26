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


        
import time
ts = time.time()

#cl= getSeq(1000000)
cl = range(0,1000000)

maxm =1
num=0
length= [0 for x in range(1000000)]

length[1] =1
for i in cl :
    #print " i si ",i
    if length[i-1]>maxm:
        maxm = length[i-1]
        num = i-1
    
    chainLen = 1
    n=i
    while(True):
        if n%2 != 0:
            n=3*n+1

        else:
            n=n/2
            #print  n
            if n<=i:
                length[i] = chainLen + length[n]
                break

        chainLen+=1
        
print "num is " ,num
print "length colletz sequence is ", maxm
print "run Time =", time.time() - ts
        
