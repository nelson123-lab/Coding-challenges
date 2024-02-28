class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (right + left)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid+1
            else:
                right = mid-1


"""
There is already a guess function defined for us so we don't need to do anything for that.
We just need to implement a binary search to find the number.
Time Complexity O(logn)
Space Complexity O(1)
"""
