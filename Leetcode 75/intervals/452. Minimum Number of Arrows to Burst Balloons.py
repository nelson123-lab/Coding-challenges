class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda i : i[1])
        arrow = 1
        prev_e = points[0][1]
        for i in range(1, len(points)):
            start, end = points[i]
            if start > prev_e:
                arrow += 1
                prev_e = end 
        return arrow

"""
- Here we are sorting the intervals based on the end element of the intervals and only need to throw an arrow if the start > previous end.
Time Complexity O(nlogn) due to sorting.
Space Complexity O(1) does the sorting inplace without using extra space.
"""
