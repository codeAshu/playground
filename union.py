def unionD(a,b):
    a.sort()
    b.sort()
    i=0
    j=0
    c=[]
    while(i+j<=len(a) + len(b) -2):
        if((i <len(a) )and (len(b)>j)):
            if ( a[i] == b[j]):
               c.append(a[i])
               i=i+1
               j=j+1
            else:
                c.append(a[i])
                c.append(b[j])
                i=i+1
                j=j+1
        else:
            if(len(a) ==0):
                c.extend(b[j:])
                j=len(b)-1
                
            if(len(b) ==0):
                c.extend(a[i:])
                i=len(a)-1
    return c

def minus(a,b):
    return list(set(a) - set(b))
