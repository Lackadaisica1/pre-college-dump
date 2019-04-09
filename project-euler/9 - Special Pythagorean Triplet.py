for a in range(1001):
    for b in range(1001):
        if a<b:
            c=(a**2)+(b**2)
            if (c**(1/2))==int(c**(1/2)):
                c=(c**(1/2))
                if a+b+c==1000:
                    print(a*b*c)
