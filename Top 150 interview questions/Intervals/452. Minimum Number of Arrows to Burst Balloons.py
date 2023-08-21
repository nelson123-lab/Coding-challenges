class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return o
        else:
            length = len(points)

        # Sorting the points by taking the end point as the key.
        points.sort(key = lambda i : i[1])

        arrow = 1
        end = points[0][1]

        for i in range(1, length):
            if points[i][0] > end:
                # Here there will be no overlapping when the end element of the first interval is less than the start of the second interval.
                arrow += 1
                # Updating the end point each time to compare with the next set of intervals. 
                end = points[i][1]
        return arrow

"""
Time complexity O(n logn)
- Here the time compelxity is mainly due to the sorting. The sorting by taking the key as the end point.
Space complexity O(1)
- No additional space is used by the algorithm. 
"""
