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
