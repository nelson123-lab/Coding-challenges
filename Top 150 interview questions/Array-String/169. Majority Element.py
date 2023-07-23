class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr_ele = 0

        for ele in nums:
            if count == 0:
                curr_ele = ele
            
            if ele == curr_ele:
                count += 1
            else:
                count -= 1
        return curr_ele
"""
The above code uses Moore voting algorithm to find the majority element in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      return sorted(nums)[len(nums)//2)

"""
The same results can be obtained by sorting.
"""
