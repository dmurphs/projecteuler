from even_fib_nums import memoize
from ten_thousand_first_prime import primes_in_range
import math    

def nth_triangular(n):
    return reduce(lambda x,y: x+y, range(1,n+1))

def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(n) + 1)) if n % i == 0)))

def first_with_500_div():
	n = 100
	while True:
		tri = nth_triangular(n)
		if len(factors(tri)) > 500:
			return tri
		n += 1

print first_with_500_div()