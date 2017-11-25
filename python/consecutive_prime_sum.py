from pylib.utils import primes_in_range

primes_under_million = filter(lambda x: x[1], [x for x in enumerate(primes_in_range(1000000))])

def prime_with_long_sum(prime_list):
	start = 2
	length = 21

it = 0
for x in primes_under_million[2:24]:
	it += x[0]

print it

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
