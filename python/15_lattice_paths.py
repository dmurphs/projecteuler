import math

def nCr(n, r):
	f = math.factorial
	return f(n)/(f(r)*f(n-r))

def num_paths(n):
	return nCr((n*2), n)

print num_paths(20)