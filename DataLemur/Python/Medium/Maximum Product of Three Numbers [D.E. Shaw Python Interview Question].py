def max_three(input):
  max_product = input[0] * input[1] * input[2]
  for i in range(len(input)-2):
    for j in range(i+1, len(input)-1):
      for k in range(j+1, len(input)):
        cur_product = input[i] * input[j] * input[k]
        if cur_product > max_product:
          max_product = cur_product
  return max_product
