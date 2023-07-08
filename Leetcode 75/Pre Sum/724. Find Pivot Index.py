class Solution:
    def pivotIndex(self, nums) -> int:
        leftSum = rightSum = 0
        i = 0
        leftSum = sum(nums[:i])
        rightSum = sum(nums[i+1:])
        if leftSum == rightSum:
            return 0
        for i in range(1, len(nums)):
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            else: pass
        return -1
    
a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))
