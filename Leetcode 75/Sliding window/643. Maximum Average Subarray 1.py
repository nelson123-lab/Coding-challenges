class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxSum = windowSum = sum(nums[:k])

        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, windowSum)

        return maxSum/k

"""
The solution works by sliding window appraoch. A window is taken with a width of k and sum is taken.
Example k = 4
Choosing different windows with size k and finding the maximum sum.
[1,12,-5,-6,50,3]
 ^        ^
    ^        ^
       ^       ^
The current sum is compared with the maximum sum each time and update the values of maxsum if current sum is greater.

Time Complexity O(n)
Space Complextiy O(1)
"""
