## Solution using Recursion
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

"""
- We are checking if n = 0 as 0! = 1
- For all other values we find the factorial buy recursive function.
"""

## Solution without recursion
def factorial(n):
  factorial = n 
  if n == 0:
    return 1
  for i in range(1, n):
      factorial *= (n-i) 
  return factorial

"""
- Here we are using a four loop finding the product multipled each times.
"""
