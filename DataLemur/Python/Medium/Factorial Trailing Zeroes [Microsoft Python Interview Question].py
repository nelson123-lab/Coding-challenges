def trailing_zeroes(n):
  
  def factorial(n):
    answer = 1
    for i in range(1, n+1):
      answer = answer * i
    return answer
  
  factorial_ = factorial(n)
  no_zeros = 0
  while factorial_ % 10 == 0:
    no_zeros += 1
    factorial_ //= 10
  
  return no_zeros

"""
- Here first we need to create a helper function to find the factorial of the number. Then we find the trailing zeros using the while loop.
Time Complexity: 𝑂(𝑛log𝑛)
Space Complexity: O(nlogn)
"""

## Optimized solution
def trailing_zeroes(n):
    no_zeros = 0
    while n > 0:
        n //= 5
        no_zeros += n
    return no_zeros

"""
Trailing Zeroes: Trailing zeroes in a number are produced by factors of 10 in the number's prime factorization. Since 
10=2×5, we need to count the pairs of factors of 2 and 5 in the factorial. However, in any factorial, the number of factors of 2 is 
usually greater than the number of factors of 5, so the number of trailing zeroes is determined by the number of factors of 5.
Time complexity O(log n)
Space Complexity O(1)
"""
