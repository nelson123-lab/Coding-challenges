class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = set()
        for i in range(n):
            j = i + 1
            k = n - 1

            while j<k:
                if nums[i] + nums[j] == -nums[k]:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans
