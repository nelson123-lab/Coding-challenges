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
        res.sort()
        return length-k

a = Solution()
print(a.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))

"""
The above solution doesn't work because the val element should be removed inplace here in the above solution a new array is created.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                nums[i] = float('inf')
                k += 1
        #  the sort() method in most programming languages, including Python, cannot handle the special value inf (infinity) directly.
        nums.sort()
        return length-k
