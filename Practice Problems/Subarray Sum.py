"""
There are 3 methods of finding the subarray over here. 
"""
class Solution:
    # This is the brute force approach we are finding all the subarrays and finding the sum of each subarray.
    """
    Time Complexity O(n^3)
    - This is because the sum() operation takes O(n) time complexity to find the sum of an array. There are 2 nested for loops as well.
    Space Complexity O(1)
    - Only one variable is used to storing the data.
    """
    def SubArraySum1(self, arr):
        # subarrays = []
        totalSum = 0
        for no in range(len(arr)):
            for j in range(no, len(arr)):
                # subarrays.append(arr[no:j+1])
                totalSum += sum(arr[no:j +1])
        return totalSum
    
    """
    Time Complexity O(n^2)
    - Here we eliminated the use of sum() operation thus reducing the time complexity to O(n^2)
    Space Complexity O(1)
    - No additional space is used here.
    """
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

    """
    Time Complexity O(n)
    - This is the optimal solution which works using mathematical formula of finding the sum of all subarray starting with start, end index each time.
    Space Complexity O(1)
    - No additional space is used by the algorithm.
    """
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
