
def divCounter(n):
    i=1
    global t
    global num
    
    count =0
    while(i<=n):
        if(n%i ==0):
            count = count+1
        i=i+1
    return count
    

t=2015
import time
ts = time.time()
while(True):
    c =  divCounter(t*(t+1)/2)
    if (c>=500):
        break
    t=t+1

print "it is ",t," th number"
print "num is", t*(t+1)/2
print "run Time ="  +str( time.time() - ts)
