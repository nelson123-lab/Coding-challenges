class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = nums
        if a + b > c and a + c > b and b + c > a:
            if len(set(nums)) == 1:
                return "equilateral"
            elif len(set(nums)) == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"

"""
Here the edge case is to check if there numbers in the array agrees to the condition that is required for 3 values to become a triangle. The sum of 2 sides should always be greater than the 3rd side for 3 values to be a
Triangle.

Time Complexity O(n)
Space Complexity O(n) due to set creation.
"""
