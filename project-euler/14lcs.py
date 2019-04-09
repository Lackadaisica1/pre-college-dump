#I never actually solved this one! :(

collatzsieve = [True] * 1000000
collatzvalues = []
collatzlengths = []
def collatzval(n):
    while (n != 1):
        if (n%2 == 0):
            n //= 2
            collatzvalues.append(n)
        else:
            n = (3 * n) + 1
            collatzvalues.append(n)
def collatz(n):
    count = 0
    while (n != 1):
        if (n%2 == 0):
            n //= 2
            ++count
        else:
            n = (3 * n) + 1
            ++count
    return count

for i in range(2, 999999):
    if i in collatzvalues:
        collatzsieve[i] = False
    elif (collatzsieve[i]):
        collatzval(i)

for k in range(0, 999999):
    if (collatzsieve[k]):
        collatzlengths.append(collatz(k))
print(max(collatzlengths))
