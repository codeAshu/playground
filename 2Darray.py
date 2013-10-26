def hori(arr):
    m=1
    lh=[]
    for i in range (0,20):
        lh =list( arr[i][:])
        pr = prod(lh)
        if pr>m:
            m = pr
    return m

def vert(arr):
    m=1
    lv=[]
    for i in range (15,16):
        lv = list(arr[:,i])
        pr = prod(lv)
        print i,"  ",pr
        if pr>m:
            m = pr
    return m

def diag(arr):
    m=1
    ld = []
    
    #left upper triangle, left t right diagnol included
    k=3
    while k<20 :
        i=k
        j=0
        while i >=0 :
            ld.append( arr[i][j] )
            i=i-1
            j=j+1
        pr=prod(ld)
        if pr>m:
            m=pr
        k=k+1
    """
    #right lower triangle till 16th column
    k=1
    while k<17:
        i=19
        j=k
        while j<20:
            ld.append( arr[i][j] )
            i=i-1
            j=j+1
        pr=prod(ld)
        if pr>m:
            m=pr
        k=k+1

        #right upper triangle right to left diagnola included
    k=16
    while k>=0 :
        i=0
        j=k
        while j<20 :
            ld.append( arr[i][j] )
            i=i+1
            j=j+1
        pr=prod(ld)
        if pr>m:
            m=pr
        k=k-1

        #left lower triangle till 16th row
    k=1
    while k<17 :
        i=k
        j=0
        while i<20 :
            ld.append( arr[i][j] )
            i=i+1
            j=j+1
        pr=prod(ld)
        if pr>m:
            m=pr
        k=k+1
       """ 
    return m
        
def prod(ls):
    print ls
    mxm =1
    if len(ls) <4:
        return 1
    for i in range(0,len(ls)-3):
        pr = ls[i]*ls[i+1]*ls[i+2]*ls[i+3]
        print ls[i]," ",ls[i+1]," ",ls[i+2]," ",ls[i+3]," ",pr
        if pr>mxm:
            mxm = pr
    return mxm
        
import numpy
arr = numpy.ndarray((20,20))
arr.fill(0)
mxm =[]
fo = open("/home/ashu/EulerProject/inputGrid", "r")
for i in range(0,20) :
    readstr = fo.read(60)
    readstr.strip('\n')
    lnum = readstr.split(' ')
    arr[i][:] = lnum
fo.close()
#mxm.append(hori(arr))
#mxm.append(vert(arr))
mxm.append(diag(arr))

print max(mxm)

