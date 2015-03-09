numstr = str(2**1000)

n = reduce(lambda x, y: int(x) + int(y), numstr)

print n