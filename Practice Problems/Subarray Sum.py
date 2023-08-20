"""
There are 3 methods of finding the subarray over here. 
"""
class Solution:
    def SubArraySum1(self, arr):
        # subarrays = []
        totalSum = 0
        for no in range(len(arr)):
            for j in range(no, len(arr)):
                # subarrays.append(arr[no:j+1])
                totalSum += sum(arr[no:j +1])
        return totalSum
    
    
    def SubArraySum2(self, arr):
        n = len(arr)
        temp, result = 0, 0
    
        # Pick starting point
        for i in range(0, n):
            temp = 0
            for j in range(i, n):
                temp += arr[j]
                result += temp
        return result
    
    def SubArraySum3(self, arr):
        totalSum = 0
        n = len(arr)

        for i in range(n):
            totalSum += arr[i] * (i + 1) * (n - i)

        return totalSum

    
a = Solution()
print(a.SubArraySum1([1, 5, 3]))
print(a.SubArraySum2([1, 5, 3]))
print(a.SubArraySum3([1, 5, 3]))

"""
Output
32
32
32
"""
