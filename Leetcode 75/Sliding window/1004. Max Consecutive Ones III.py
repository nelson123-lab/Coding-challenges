class Solution:
    def longestOnes(self, nums, k):
        left  = right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            # The time when 2 zeros are already replaced with ones.
            if k < 0:
                if nums[left] == 0:
                    k += 1
            
                left += 1

        return right- left + 1

a = Solution()
print(a.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))

"""
The logic behind solving this problem is by understanding the technique.
k value represents the number of 0's that we can replaced with 1. 
We can keep track of the k value by increasing and decreasing it when there is 1 and 0 respectively.
"""
