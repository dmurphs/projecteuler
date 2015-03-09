from circular_primes import is_prime

def collatz(n):
  if n == 1:
    return []
    
  elif n % 2 == 0:
    return [n/2] + collatz(n/2)
  
  else:
    return [3*n+1] + collatz(3*n+1)
    
primes = filter(is_prime, range(1000000))

l = [len(collatz(n)) for n in primes]

maximum = sorted(l)[-1]

for num,val in enumerate(l):
  if val == maximum:
    print primes[num],val