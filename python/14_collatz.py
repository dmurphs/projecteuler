from operator import itemgetter

def collatz(n):
  if n == 1:
    return []

  elif n % 2 == 0:
    return [n/2] + collatz(n/2)

  else:
    return [3*n+1] + collatz(3*n+1)

lengths = [(n, len(collatz(n))) for n in range(1,1000000)]

max_seq = max(lengths, key=itemgetter(1))
print(max_seq)
