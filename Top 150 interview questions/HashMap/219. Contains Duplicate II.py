class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for idx in range(len(nums)):
            if nums[idx] in hashmap and abs(idx-hashmap[nums[idx]]) <= k:
                return True
            hashmap[nums[idx]] = idx
        return False

"""
Time Complexity O(n)
- Here only 1 iteration is happening, so the time complexity is O(n)
Space Complexity O(n)
- We are using a hashmap to keep track of the elements within the list. It is O(min(n, k) but the worst case space complexity is O(n).
"""
