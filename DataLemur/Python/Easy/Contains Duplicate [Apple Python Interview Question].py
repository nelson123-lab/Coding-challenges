# Solution using set
def contains_duplicate(input)-> bool:
  return False if len(set(input)) == len(input) else True

"""
Here we are checking if the length of the set using the input is same as the length of the input.
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Solution using dictionary
def contains_duplicate(input):
  seen = {}
  for i in input:
    if i in seen:
      return True
    seen[i] = True
  return False

"""
Here we are using a dictionary to keep track of the duplicates present in the list. If anything is repeated return True else False.
Time Complexity: O(n)
Space Complexity: O(n)
"""
