class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for idx, ele in enumerate(nums):
            if ele == 0:
                nums.pop(idx)
                count += 1
            else:
                pass
        nums = nums + [0]* count
        return nums
    
ans = Solution()
print(ans.moveZeroes([0,1,0,3,12]))