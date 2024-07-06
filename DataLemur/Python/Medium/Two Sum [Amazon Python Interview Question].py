def two_sum(input: list[int], target) -> list[int]:
  d = {}
  for i in range(len(input)):
    cur_value = input[i]
    diff = target - cur_value
    if diff in d:
      return [d[diff], i]
    d[cur_value] = i
  
  return [-1, -1]

"""
Time Complexity O(n)
Space Complexity O(n)
"""
