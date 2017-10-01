import math

def memoize(f):
    cache  = {}
    def decorated(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return decorated

def primes_in_range(n):
    isPrimeList = [True for x in range(0, n+1)]
    isPrimeList[0] = False
    isPrimeList[1] = False

    upper = int(math.sqrt(n))
    for x in range(upper):
        if isPrimeList[x]:
            index = x*x
            while index <= n:
                isPrimeList[index] = False
                index = index + x
    return isPrimeList