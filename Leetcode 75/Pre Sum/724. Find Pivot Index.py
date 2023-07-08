class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        i = 0
        leftSum = sum(nums[:i])
        rightSum = sum(nums[i+1:])
        if leftSum == rightSum:
            return 0
        for i in range(len(nums)):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            else: pass
        return -1
