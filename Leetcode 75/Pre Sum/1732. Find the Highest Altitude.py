class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curralt = maxalt = 0
        for i in range(len(gain)):
            curralt += gain[i]
            maxalt = max(curralt, maxalt)
        return 0 if maxalt < 0 else maxalt
"""
Storing the highest altitude each time and finally returing the maximuum altitude point.
"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxaltittude = 0
        currSum = 0
        for i in range(len(gain)):
            currSum = currSum + gain[i]
            maxaltittude = max(maxaltittude, currSum)

        return maxaltittude
"""
Here the algorithm checks for curr sum and checks for the maximum values each time.
Time Complexity O(n)
Space Complexity O(1)
"""
