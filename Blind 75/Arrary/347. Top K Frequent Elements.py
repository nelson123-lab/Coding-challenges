class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        
        # Count the frequency of each number
        for i in nums:
            ref[i] = ref.get(i, 0) + 1
        
        # Sorting the hashmap values according to the values
        sorted_items = sorted(ref.items(), key = lambda x: x[1], reverse=True)
        
        # Extract the top k elements
        top_k = [item[0] for item in sorted_items[:k]]
        
        return top_k

"""
- Here we are keeping a ref hashmap to keep track of the elements count so that we can extract the top K elements.
- sorting the dictionary based on values to get the top k keys.
Time Complexity O(n logn)
Space Complexity O(n)
"""
