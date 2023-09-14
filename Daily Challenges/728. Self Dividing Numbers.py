class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for digit in range(left, right+1):
            if digit < 10:
                res.append(digit)
            else:
                count = 0
                for ele in str(digit):
                    
                    if int(ele) == 0 or digit % int(ele) != 0:
                        break
                    else: count += 1
                if count == len(str(digit)):
                    res.append(digit)  
                else: pass
        return res

"""
Time Complexity O(n*m)
Space Complexity O(n) because of the requested output
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for digit in range(left, right+1):
            if all(int(ele) != 0 and digit % int(ele) == 0 for ele in str(digit)):
                res.append(digit)
        return res

"""
Same complexities as of above but of minimal line code. This avoids the usage of count or flag to check if the for loop worked successfully.
"""
        
