def memoize(f):
	cache  = {}
	def decorated(n):
		if n in cache:
			return cache[n]
		else:
			cache[n] = f(n)
			return cache[n]
	return decorated

@memoize
def fib(n):
	return n if n < 4 else fib(n-1) + fib(n-2)

def even_fib_sum(upper_bound):
	i = 2
	sum = 0
	while True:
		x = fib(i)
		if x >= upper_bound:
			return sum
		sum += x
		# even numbers in fib repeat every three terms (look up proof)
		i += 3

print even_fib_sum(4000000)