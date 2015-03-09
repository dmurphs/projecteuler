import math

def get_product():
    return [a*b*math.sqrt(a**2 + b**2) for a in range(1,1000) for b in range(1,1000) if (a+b+math.sqrt(a**2 + b**2)) == 1000]

print get_product()
