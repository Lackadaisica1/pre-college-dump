arrayboolean = [True] * 2000000
for i in range(2, 1999999):
    if arrayboolean[i]==True:
        for j in range((i**2), 2000000, i):
            arrayboolean[j]=False
alop = [i for i, e in enumerate(arrayboolean) if e==True]
sum1=0
for n in alop:
    sum1+=n
print(sum1-1)
