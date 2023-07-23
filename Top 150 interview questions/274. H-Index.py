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
- This problem is solved using binary search. The array is first sorted in ascending order.
- For H index to be valid there should be same no of papers published by the author with the same or more number of citations. Here the first 
condition checks that. This only works after sorting the algorithm.
- The final part returns the maximum value of h-index among the array the value.
eg: [1,2,4,6,1,5]
In this example after the iterations the high will become 2 and low will become 3 that's when the while loop stops. The algorithm will 
return n-low => 6-3 = 3. Here it is returning the highest value that h index can obtain.
"""
            
