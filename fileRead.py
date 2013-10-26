
def fprod(n):
    prod =1
    for i in range (0,5):
        print n[i]
        prod = prod*n[i]
    return prod
    
def chomp(s):
    if s[-1] == '\n':
        return s[:-1]
    else:
        return s

max= 0
i=1
prod =  1
fo = open("/home/ashu/EulerProject/input.txt", "r")
while (True):
    str = fo.read(5);
    num = list(str)
    num = chomp(num)
    num = map(int,num)
    
    print num

    if len(num) == 5:
        prod = fprod(num)    
        print "product is ", prod
        if prod > max :
            max=prod
        # Reposition pointer at the beginning once again
        position = fo.seek(i, 0)
        print "i is ", i
        i=i+1
    else:
        fo.close()
        break

print max
