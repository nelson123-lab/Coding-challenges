# Solution using Set method.
def intersection(a, b):
  A, B = set(a), set(b)
  return list(A.intersection(B))
  
# One-liner
def intersection(a, b):
  return list(set(a).intersection(set(b)))

"""
- Here we are first converting the list to set A and set B and then finding the intersectin between them.

Time Complexity O(n + m)
Space Complexity O(n + m) 
- Converting a list to a set is an O(n) operation.
"""

# Solution using Lists
def intersection(a, b):
  common = []
  for i in a:
    if i in b:
      common.append(i)
    else: pass
  return common

# One-liner
def intersection(a, b):
  return [i for i in a if i in b]

"""
- This uses 2 lists itself each time it iterates through the list A and checks for the value in list B.
- This is a bad approach as the search operation takes O(n) time complexity "if i in b".

Time Complexity O(n*m)
Space Complexity O(n)
"""

