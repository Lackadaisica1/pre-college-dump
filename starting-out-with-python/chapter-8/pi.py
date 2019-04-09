import math
a = 1
b = 1 / (math.sqrt(2))
t = 1 / 4
p = 1
for i in range(10):
    an = (a + b) / 2
    bn = math.sqrt(a * b)
    tn = t - p * ((a - an) ** 2)
    pn = 2 * p
    a = an
    b = bn
    t = tn
    p = pn
pi = ((an + bn) ** 2) / (4 * tn)
print(pi)
