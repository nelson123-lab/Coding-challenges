class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        output = 0
        prev_s, prev_e = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= prev_e:
                prev_e = end
            else:
                output += 1
                prev_e = min(end, prev_e)
        return output

"""
Time Complexity O(nlogn)
Space Complexity O(n)
"""
