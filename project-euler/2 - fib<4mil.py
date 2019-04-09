def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)

def fibsum(n):
    if fib(n) < 4000000:
        if fib(n)%2==0:
            return fib(n) + fibsum(n+1)
        else:
            return fibsum(n+1)
    else:
        return 0
n=0
sum2=fibsum(n)
print(sum2)
    
