from ten_thousand_first_prime import primes_in_range

def get_primes_under(n):
	l = primes_in_range(n)
	return [x for x in range(len(l)) if l[x]]

def sum_primes_under_n(n):
	return reduce( lambda x,y : x + y, get_primes_under(n))

print sum_primes_under_n(2000000)