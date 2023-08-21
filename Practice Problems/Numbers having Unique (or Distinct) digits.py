"""
Here 2 solutions are explained one is a brute force approcah and the other one an optimal appraoch that works in O(n) time complexity.
"""
class Solution:
    def uniqueDigitsFinder1(self, arr):
        # Iterating through the intervals
        res = []
        for start, end in arr:
            # checking the elements within the numbers
            count = 0
            while start <= end:
                if len(set(str(start))) != len(str(start)):
                    start += 1
                else:
                    start += 1
                    count += 1
            res.append(count)
        return res
        
                
    def uniqueDigitsFinder2(self, arr):
        res = []
        for start, end in arr:
            count = 0
            for i in range (start, end + 1):
                num = i;
                visited = [0,0,0,0,0,0,0,0,0,0]
                 
                while (num):
                    if visited[num % 10] == 1:
                        break;
                    visited[num % 10] = 1
                    num = (int)(num / 10)
                     
                if num == 0:
                    count += 1
            res.append(count)
        return res

a = Solution()
print(a.uniqueDigitsFinder1(arr = [[1, 5], [7, 12], [22, 31]]))
print(a.uniqueDigitsFinder2(arr = [[1, 5], [7, 12], [22, 31]]))

"""
Output
[5, 5, 9]
[5, 5, 9]
"""
                
