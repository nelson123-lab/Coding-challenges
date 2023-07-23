class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high, mid = 0, n-1, 0
        citations.sort()
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
This problem is solved using binary search. The array is first sorted in ascending order.
"""
            
