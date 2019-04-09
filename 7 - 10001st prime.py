arrayboolean = [True] * 1000000
for i in range(2, 999999):
    if arrayboolean[i]==True:
        for j in range((i**2), 1000000, i):
            arrayboolean[j]=False
alop = [i for i, e in enumerate(arrayboolean) if e==True]
print(alop[10002])
    
