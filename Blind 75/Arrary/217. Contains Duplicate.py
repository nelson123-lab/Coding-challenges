class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

"""
- The logic is when the no of occurances of a particular element is more then the length will be greater than a set(array).
- Set does not contain duplicate elements.
"""
