#17 number letter counts

num_dict={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

ones = [num_dict[i] for i in range(1,10)]
teens = [num_dict[i] for i in range(10,20)]
tens = [num_dict[i] for i in range(20, 100, 10)]
hundreds = [num + 'hundred' for num in ones]
thousand = 'onethousand'

def get_len(num_len_list):
  return reduce(lambda x,y: x+y, num_len_list)

len_ones = get_len(map(lambda x: len(x), ones))
len_teens = get_len(map(lambda x: len(x), teens))
len_tens = reduce(lambda x,y: x+y, [10*len(ten) + len_ones for ten in tens])
len_hundreds = reduce(lambda x,y: x+y, [100*len(hund) + len_tens + len_teens + len_ones + (99*3) for hund in hundreds])
len_thousand = len(thousand)

total = len_ones + len_teens + len_tens + len_hundreds + len_thousand

print total