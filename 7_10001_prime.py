import math

def primes_in_range(n):
	l = [True for x in range(0, n+1)]
	l[0] = False
	l[1] = False
	upper = int(math.sqrt(n))
	for x in range(upper):
		if l[x]:
			index = x*x
			while index <= n:
				l[index] = False
				index = index + x
	return l

def get_10001_prime():
	found = False
	n = 10001
	while not found:
		l = primes_in_range(n)
		prime = 0
		for x in range(len(l)):
			if l[x]:
				prime += 1
			if prime == 10001:
				return x
		n += 10000

print get_10001_prime()