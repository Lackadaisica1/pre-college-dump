alop=[]
n = 600851475143
def isprime(n):
    z=5
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False
    while z*z<=n:
        if n%z==0 or n%(z+2)==0:
            return False
        z+=6
    return True


for i in range(3, int(600851475143**.5), 2):
    if n%i==0:
        if isprime(i):
            alop.append(i)


print(max(alop))

    
