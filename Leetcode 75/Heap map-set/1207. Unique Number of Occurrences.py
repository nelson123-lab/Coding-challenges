class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = []

        for i in set(arr):
            curr_count = arr.count(i)
            if curr_count not in count:
                count.append(curr_count)
            else:
                return False
        return True
"""
- Coverting the list to set inorder to reduce the no of elements to iterate.
- Keeping a count reference and checking whether the no of occurances are already present in the list.
"""
