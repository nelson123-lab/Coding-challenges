class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        l, r = 0, len(costs) - 1
        res = 0
        pq2, pq1 = [], []

        while k:

            while len(pq1) < candidates and l <= r:
                heapq.heappush(pq1, costs[l])
                l += 1

            while len(pq2) < candidates and l <= r:
                heapq.heappush(pq2, costs[r])
                r -= 1

			# This is the case when element in the costs array <= candidates
            if len(pq1) == 0:
                heapq.heappush(pq1, float("inf"))
            elif len(pq2) == 0:
                heapq.heappush(pq2, float("inf"))

			# In case of same values in both priority queues will take first priority queue value
            res += heapq.heappop(pq1) if pq1[0] <= pq2[0] else heapq.heappop(pq2)           
            k -= 1

        return res
