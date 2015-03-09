#52

def find():
  x = 1
  while True:
    nums = [i for i in str(x)]
    if contains_same(x,nums):
      return x
    x+=1
    
def contains_same(x, nums):
  numstrs = (substr for i in range(1,7) for substr in str(i*x))
  for numstr in numstrs:
    if numstr not in nums:
      return False
      
  return True

print find()