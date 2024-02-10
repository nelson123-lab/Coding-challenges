class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True
"""
This solution just passes the test case since the person who plays first always wins in this case. This problem should be solved using dynamic progrogramming.
"""

"""
The below solution is a math solution written by someone.
"""
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @cache
        def score(i: int, j: int) -> int:
            return (i < j) and max(piles[i] + score(i + 1, j), piles[j] + score(i, j - 1))
        
        return score(0, len(piles) - 1)
"""
Credits: https://leetcode.com/problems/stone-game/solutions/3573069/python-short-and-clean-functional-programming
"""
