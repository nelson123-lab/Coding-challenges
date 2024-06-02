import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = nums[:k] # populate heap with first k elements
        heapq.heapify(n)
		
        # loop through rest of array and pushpop largest elements
        for num in nums[k:]:
            if num > n[0]:
                heapq.heappushpop(n, num)
        
        return n[0]

