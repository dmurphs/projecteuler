from fractions import gcd

def lcm(num_list):
	return reduce(lambda x,y : x*y / gcd(x,y), num_list)


# only need to check 11 to 20
print lcm(range(10,21))