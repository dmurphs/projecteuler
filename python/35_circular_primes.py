# 35 find circular primes under a given number n
from pylib.utils import is_prime
import math

def sieve(n):
  primes = [True]*n
  primes[0] = primes[1] = False

  for (index, val) in enumerate(primes):
    if val:
      for x in range(index*index, n, index):
        primes[x] = False

  return primes

def rotations(numstr):
    l = [numstr]
    x = 0
    while x < len(numstr):
        numstr = numstr[1:] + numstr[0]
        l.append(numstr)
        x += 1
    return l

def is_circular(n):
    rots = rotations(str(n))
    for num in rots:
        if not is_prime(int(num)):
            return False
    return True

def all_odd(n):
    for x in str(n):
        if int(n) % 2 == 0:
            return False
    return True

def circular_primes_under(n):
  possibilities = [x[0] for x in enumerate(sieve(n)) if x[1] and (all_odd(x[0]) or x[0] == 2)]
  return filter(is_circular, possibilities)
