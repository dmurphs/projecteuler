def is_power_of_ten(n):
  if str(n)[0] != '1':
    return False
  for (n,val) in enumerate(str(n)):
    if n>0 and val != '0':
      return False
  return True
  
nums = (str(i) for i in range(1,186000))
numstr = ''.join(nums)

ten_pow_nums = (numstr[i-1] for i in range(len(numstr)) if is_power_of_ten(i))

print reduce(lambda x,y: int(x)+int(y), ten_pow_nums)
