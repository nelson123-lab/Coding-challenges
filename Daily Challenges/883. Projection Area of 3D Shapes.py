class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy = sum([len([i for i in g if i != 0]) for g in grid])
        zx = sum([max(g) for g in grid])
        yz = sum([max(g) for g in list(zip(*grid))])
        
        return xy + yz + zx

"""
Time complexity O(n)
Space complexity O(n)
"""
