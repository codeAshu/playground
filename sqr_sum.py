
def sqDiff(n):
    s_sq =0
    sq_s=0
    for i in range (1,n+1):
        s_sq=s_sq+i*i

    sq_s = pow(n*(n+1)/2,2)

    diff = sq_s - s_sq

    print diff


sqDiff(100)
