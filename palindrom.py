allNo = []
def checkP(n):
   return int(str(n)[::-1]) ==n


import time
ts = time.time()
i=999
num =0
maxpal
while i>100:
    j=i
    while j>100:
       num = i*j
      # print num
       if checkP(num) and num>maxpal:
           maxpal = num
       j=j-1
    i=i-1
print maxpal
print "run Time ="  +str( time.time() - ts)







