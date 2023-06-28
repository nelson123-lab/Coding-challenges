class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for idx, ele in enumerate(gain):
            alt.append(alt[-1]+gain[idx])
        return max(alt)
