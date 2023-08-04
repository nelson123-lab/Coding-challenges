class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [i+1, j+1]
            if s > target:
                j-= 1
            else:
                i += 1    
        return []

"""
Here two pointers are added and checks whether the sums equals to target.
Time Complexity O(n)
Space Complexity O(1)

"""
