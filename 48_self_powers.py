def power_sum(n):
	return reduce(lambda x,y: x + y, [x**x for x in range(1, n+1)])

print str(power_sum(1000))[-10:]