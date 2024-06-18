def missing_int(input: list[int])-> int:
  input.sort()
  for i in range(len(input)):
    if i != input[i]:
      return i
  return len(input)
    
"""
Explanation
- Here the input follows a pattern of the range so we can first sort the elements and check for any element if not present.
Time Complexity O(n logn)
Space Complexity O(n)
"""

def missing_int(input: list[int])-> int:
    gauss_sum = len(input)*(len(input)+1) // 2
    actual_sum = sum(input)
    return gauss_sum - actual_sum

"""
- Here gauss sum is the sum of n numbers from 1 to n using the formula n(n+1)//2
- If we substract the actual sum from the gauss sum we get the number.
"""
