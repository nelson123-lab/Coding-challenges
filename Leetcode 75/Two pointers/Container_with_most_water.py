class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, maxArea = 0, len(height) - 1, 0

        while left < right:
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currArea)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

        return maxArea

"""
- Here it uses two pointer approach to find the maxArea of water contained between the two pillars.
- Area can be found by finding the minimum height value among the two pillars multiplied with distance.
Time Complexity O(n)
Space Complexity O(1)
""""
