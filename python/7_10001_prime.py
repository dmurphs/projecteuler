from pylib.utils import primes_in_range

def get_10001_prime():
	n = 10001
	while True:
		primeList = primes_in_range(n)
		number_of_primes = 0
		for x in range(len(primeList)):
			if primeList[x]:
				number_of_primes += 1
			if number_of_primes == 10001:
				return x
		n += 10000

print(get_10001_prime())