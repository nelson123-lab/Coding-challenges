class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = [(-n, c) for (c, n) in Counter(s).items()]

        heapq.heapify(max_heap)
        result = ''

        while max_heap:
            freq, c = heapq.heappop(max_heap)

            if result and result[-1] == c:
                return ''
            
            result += c
            freq += 1

            if freq != 0:
                max_heap.append((freq, c))

        return result
