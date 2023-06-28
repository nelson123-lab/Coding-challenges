class Solution:
    def getAverages(self, nums, k):
        n = len(nums)
        avgs = [-1] * n

        for i in range(n):
            start = max(0, i - k)
            end = min(n - 1, i + k)

            if end - start + 1 >= 2 * k + 1:
                subarray_sum = sum(nums[start:end+1])
                avgs[i] = subarray_sum // (2 * k + 1)

        return avgs

# Failing for long array input needs to be fixed.
