hugeassnumber = 2**1000
hugeasssum = 0
n = 0
while hugeassnumber != 0:
    n = hugeassnumber % 10
    hugeasssum += n
    hugeassnumber //= 10
print(hugeasssum)
