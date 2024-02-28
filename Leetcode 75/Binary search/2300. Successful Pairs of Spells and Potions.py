class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = []
        for s in spells:
            idx = len(potions)
            l, r = 0, len(potions)-1
            while l <= r:
                mid = (l + r)//2
                if s*potions[mid] >= success:
                    r = mid - 1
                    idx = mid
                else:
                    l = mid + 1
            res.append(len(potions) - idx)
        return res

"""
Here the solution requires a binary search implementation
Time Complexity O(n*logM)
Space Complexity O(n)
"""
