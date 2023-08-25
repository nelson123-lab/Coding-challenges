class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        LIS=[1]*n
        
        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    LIS[i]=max((LIS[i]), (LIS[j]+1))
        
        return max(LIS)

"""
Time Compelxity O(n^2)

Space Complexity O(n)
"""
