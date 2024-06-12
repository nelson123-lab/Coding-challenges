def fizz_buzz_sum(target):
  fizz_buzz_sum = 0
  for i in range(1, target):
    if i % 3 == 0 or i % 5 == 0:
      fizz_buzz_sum += i
  return fizz_buzz_sum

"""
- Here we just need to check if the number below the target are exactly divisible by 3 or 5.
- If they are divisible we need to sum them together resulting in the fizz buzz sum.
"""
