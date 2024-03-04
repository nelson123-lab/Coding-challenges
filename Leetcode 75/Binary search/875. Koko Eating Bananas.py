class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)

        while l < r:

            mid = (l + r) // 2
            c = 0
            for j in piles:
                c += ((j-1)//mid)+1
            if c > h:
                l = mid + 1
            else:
                r = mid
        return l

  """
  The above solution uses binary search approach to find the no of bannanas the koko eats per hour to eat all pile of bannanas.
  Time Complexity O(n)
  Space Complexity O(1)
  """
