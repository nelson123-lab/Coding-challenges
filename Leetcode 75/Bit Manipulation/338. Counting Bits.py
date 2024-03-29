class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0]
        for i in range(1, n + 1):
            output.append(output[i >> 1] + i % 2)
        return output

"""
- This count is calculated by adding the count of set bits in i // 2 (right shift by 1) to the least significant bit (i % 2).
Time Complexity O(n)
Space Complexity O(n)
"""
