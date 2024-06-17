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
