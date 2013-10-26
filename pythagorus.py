
def pytha(sum):
    n=1
    m=0
    while(True):
        m=0
        while(m<n):
            if n*(n+m) ==sum/2:
                return [n,m]

            m=m+1
        n=n+1


res = pytha(1000)
n=res[0]
m=res[1]

a=pow(n,2) - pow(m,2)
b= 2*n*m
c=pow(n,2) + pow(m,2)

print a,b,c
if pow(c,2) == pow(a,2)+pow(b,2): print "Done"
print a*b*c

     
