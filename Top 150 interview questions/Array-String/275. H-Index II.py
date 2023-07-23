class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high, mid = 0, n-1, 0
        while low <= high:
            mid = low + (high-low)//2
            if citations[mid] == (n-mid):
                return citations[mid]
            elif citations[mid] > (n-mid):
                high = mid-1
            else:
                low = mid+1
        return n-low

"""
The only difference between the H-index and H-index II problem is that the array is sorted in ascending order by default. The algorithm is
exactly similar.

Time Complexity O(logn)
- This is due to the use of binary search through the citations array. This uses a logarithmic time complexity.
Space Complexity O(1)
- This algorithm works in constant time. There O(1).
"""
