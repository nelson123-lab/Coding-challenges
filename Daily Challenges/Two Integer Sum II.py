class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currsum = numbers[left] + numbers[right]
            if currsum > target:
                right -= 1
            elif currsum < target:
                left += 1
            else:
                return [left + 1, right + 1]

"""
Here we are using a two-pointer approach.

Time Complexity O(n)
Space Complexity O(1)
"""
