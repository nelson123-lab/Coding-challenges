# To find the indexes of two elements that add up to the target.
# Brutforce Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterating through the number list.
        for i in range(len(nums)):
          """
          Finding the difference between each elements and the target inorder to check whether 
          the difference exists within the list and return the indices of the both.
          """
            a = target - nums[i]
            if a in nums and nums.index(a) != i:
                return [i, nums.index(a)]
            else:
                pass
"""
This solution passes all the test case but the time complexity is O(n^2). Here nested for loop is present. The in and .index operation works in 
O(n) time complexity and it is within the for loop. Therefore, O(n^2).
"""
# Optimal Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for idx, ele in enumerate(nums):
            diff = target - ele
            if diff in ref:
                return [ref[diff], idx]
            ref[ele] = idx
        return
"""
Time Complexity O(n)
Here a dictionary is used within the forloop. The insertion into the dictionary and search happens in constant time.
Space Complextiy O(n)
Here the space used depend on the input. The worst case when no two elements add up to the target all the elements will stored in the dictionary.
"""
