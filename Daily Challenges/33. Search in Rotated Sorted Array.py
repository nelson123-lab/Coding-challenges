class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)
"""
Time COmplexity O(n)
Space Complexity O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
       left, right = 0, len(nums)-1
       while left <= right:
            if nums[left] == target:
               return left
            elif nums[right] == target:
                return right
            else:
                left += 1
                right -= 1
       return -1

"""
Time Complexity O(n)
Space Complexity O(1)
"""

"""
The below solution uses binary search to acheive a time complexity of O(logn)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

"""
Time Complexity O(logn)
Space Complexity O(1)
"""
