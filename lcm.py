import Prime_no
pl =  Prime_no.prime_list(1,20)
print pl

def IsLCM(n):
    
    for i in range(1,20):
        if(n%i == 0):
            continue
        else :return False
    if(i==20):
        return True
    
m=1
for i in range(0, (len(pl)-1) ):
    
    m = m*pl[i]
    print m,i
#while(not (IsLCM(m)) ):
  #  m= m+1

print m
    


