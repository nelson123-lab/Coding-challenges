class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            d[i] = d.setdefault(i, 0) + 1
        d = dict(sorted(d.items(), key = lambda x: (-x[1], x[0])))
        keys = list(d.keys())
        return keys[:k]

"""
Time Complexity O(nlogn)
Space Complexity O(n)
"""
