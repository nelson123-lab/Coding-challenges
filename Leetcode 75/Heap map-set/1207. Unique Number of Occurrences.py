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
- If any value's occurance repeat return False.
Time Complexity O(n2)
Space Complexity O(n)
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        return len(counts.values()) == len(set(counts.values()))

"""
Here we are using a hashmap to keep track of the elements present in the array.
Time complxity O(n)
Space complexity O(1)
"""
