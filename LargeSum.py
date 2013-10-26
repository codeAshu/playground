def vert(arr):
    global carry
    carry =0
    m=1
    lv=[]
    addlist = []
    for i in range (49,-1,-1):
        #print i
        lv = list(arr[:,i])
        #print lv
        print "result for", i,"th column" 
        addlist.append( add(lv) )

    addlist.append(carry)     
    return addlist[-1::-1]
#######################################
def add(ls):
    sm= 0
    global carry
    #print ls
    sm = sum(ls)
    print "sum is ",sm, "carry is ",carry,"total sum is ",sm+carry
    sm = sm + carry
    
    sumStr = str(sm)
    carrystr = sumStr[0:-3]
    #print "carry str id ",carrystr
    carry = int(carrystr)
    print "last digit is ",sumStr[-3]
    print "carry for next time is ",carry
    return sumStr[-3]
#############################################

import numpy
arr = numpy.ndarray((100,50))
arr.fill(0)
fo = open("/home/ashu/EulerProject/largeSumInput.txt", "r")
for i in range(0,100) :
    readstr = fo.read(51)
    readstr = readstr.strip('\n')
    row = list(readstr)
    arr[i][:] = row
fo.close()
print arr
res  = vert(arr)
print "first 10 numbers are", res
