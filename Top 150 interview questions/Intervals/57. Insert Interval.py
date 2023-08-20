class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Appeding the new interval to the list.
        intervals.append(newInterval)
        intervals.sort(key = lambda i : i[0])
        out = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = out[-1][1]

            if start <= lastEnd:
                out[-1][1] = max(lastEnd, end)
            else:
                out.append([start, end])

        return out

"""
Time complexity O(n logn)
- This problem is similar to the merge intervals problem. The only difference is that we need to add a new interval to the list.
- This can be done by just appending the the new Interval first and merge intervals.
Space Complexity O(n)
- This is the space used by the out array.
"""
