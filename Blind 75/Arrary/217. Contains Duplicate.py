class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

"""
- The logic is when the no of occurrences of a particular element is more then the length will be greater than a set(array).
- Set does not contain duplicate elements.

Time Complexity O(n)
Space Compelxity O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:        
        ref = set()
        for ele in nums: 
            if ele not in ref:
                ref.add(ele)
            else:
                return True
        return False
"""
Here we are keeping a set to keep track of the element
Time Complexity O(n)
Space Complexity O(n)
"""
