# A program to calculate the largest palindromic product of two 3 digit
# Numbers
alopr = []
for i in range(100, 1000):
    for x in range(100, 1000):
        z = x*i
        alopr.append(z)
alopa = []

def ispalindrome(n):
    lf = []
    lr = []
    z = str(n)
    for ch in z:
        lf.append(ch)
    for i in range(-1, (-1-len(z)), -1):
        lr.append(z[i])
    if lf==lr:
        return True

    
for n in alopr:
        if ispalindrome(n):
            alopa.append(n)
print(max(alopa))
