class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting according to the intervals to keep track of the start element.
        intervals.sort(key = lambda i : i[0])
      
        out = [intervals[0]]
        for start, end in intervals[1:]:
            # The method is used to compare the last set of intervals in the list to the latest interval everytime.
            lastEnd = out[-1][1]

            if start <= lastEnd:
                # Taking the max each time to update the maximum element to the output array.
                out[-1][1] = max(lastEnd, end)
            else:
                # When to consecutive intervals doesn't have any common elements to merge. We just append the elements.
                out.append([start, end])
        return out

"""
Time Complexity O(n logn)
- This is the time complexity for sorting the list.
Space Complexity O(n)
- Here the out list depends on the input size. If the input contains distinct intervals, then there will be n distinct intervals as the worst case.
"""
