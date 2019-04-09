# formula for lattice paths: given that paths from corner to corner
# are the same as paths from (0, 0) to (n, k), number of paths
# equals choose n + k over n
def factorial(n):
    result = 1
    # up to but not including why is everything is an object aaaa
    for i in range(1, (n+1)):
        result *= i
    return result
n = factorial(40)
k = factorial(20)
nminusk = factorial(20)
answer = (n//(k*nminusk))
print(answer)
