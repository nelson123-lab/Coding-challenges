class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prevVal, currVal = 0, 0
        res = 0
        for val in reversed(s):
            currVal = romanNum[val]
            if prevVal > currVal:
                res -= currVal
            else:
                res += currVal
            prevVal = currVal
        return res

"""
Here the basic idea is that when we try to change the Roman Numeral in the reverse order, It's easier to find the corresponding Numericals.
When you check with the previous value and substract from the res, the exceptions like 'IV', 'IX' etc.
Time Complexity O(n)
- Here the reversing and iterating through the array happens in different steps. So the time complexity of the algorithm is O(n).
Space Complexity O(1)
- Here the algorithm is independent on the input size. So the space complexity is O(1).
"""
