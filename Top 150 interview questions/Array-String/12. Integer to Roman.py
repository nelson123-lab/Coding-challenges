class Solution:
    def intToRoman(self, num: int) -> str:
        int_roman = {1000: "M", 900: "CM", 500: "D", 400: 'CD', 100: "C", 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: "IV", 1: "I"}
        res = ""
        for i in int_roman:
            while num>=i:
                num-= i
                res += int_roman[i]
        return res

"""
Time Complexity O(n)
- Here n is the number of intergers inside the num.
Space Complexity O(1)
- Uses constant amount of additional space.
"""
