# A program to find the difference between the sum of first hundred squares
# And the square of the first hundred numbers summed
def squareadd(n):
    if n==0:
       return 0 
    else:
        return (n**2) + squareadd(n-1)
sum1 = 0
for i in range(0, 101):
    sum1+=i
print((sum1**2)-(squareadd(100)))
