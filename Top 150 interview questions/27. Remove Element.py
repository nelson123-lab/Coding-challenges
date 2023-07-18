class Solution:
    def removeElement(self, nums, val) -> int:
        res = []
        k = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                res.append(nums[i])
            else:
                k += 1
        # res[length-k:] = ["_"]*k
        return res

a = Solution()
print(a.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
