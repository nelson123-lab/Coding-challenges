"""
We cannot sort the array to find the longest consecutive list of numbers. It is required that the time complexity should be O(n). The sorting makes it O(nlogn) time complexity itself.
"""

"""
This is a solution with sorting.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Checking if the length is 0, then there is no consecutive elements.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        max_seq, curr_max = 1, 1
        # The list contains duplicates as well we need to get rid of that. 
        nums = list(set(nums))
        # Sorting it to check the longest consecutive numbers.
        nums.sort()
        # The start and end should be initialized after the making the modification of the lists. Since converting the list to set reduces the number of elements.
        # If this is initialized before modification it will result in index out of the range error.
        start, end = 0, len(nums)
        while start < (end - 1): # end -1 to avoid the index out of the range error.

            if nums[start + 1] - nums[start] == 1:
                curr_max += 1
            else:
                curr_max = 1
            # we need to increase the start value so that iteration should happen.
            start += 1
            if curr_max > max_seq:
                max_seq = curr_max
        return max_seq
"""
Time Complexity O(nlogn)
- Here the worst complexity is O(n log n) since sorting is done.
Space Complexity O(n)
- A set is used to store the eleements which results in O(n) space complexity.
"""

"""
Intuition
- When we see the array of numbers if the length of the array is 0, then the longest consecutive numbers will be 0. Similarly 1, in the case of when lenght is 1.
- The important thing over here is that we should solve the question in O(n) so we can't use any sorting techniques which will result in a time complexity of O(n log n) for merge, heap, 
quick and tim sort. O(n^2) for Bubble, selection and insertion sort.
- The main idea here is to identify the starting of the sequence. This can be identified by checking whether (no-1) exists in the set. If it doesn't the length of the sequence will be zero. We can 
identify the length of the sequence by checkig whether (no+1) exists in the set each time which results in the length of the sequence.

Approach
- Here, if we are checking whether (no-1) and (no+1) exists in the list, it will result in an O(n) time complexity. We anyway require a for loop to iterate through the list. Thus the time complexity becomes O(n^2).
- Inorder to reduce the time complexity we are converting the list to a set. The process takes only O(n) time complexity. Searching an element within the set is a O(1) time 
complexity process since the set uses a hashtable structure.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Checking if the length is 0, then there is no consecutive elements.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        

        numset = set(nums)
        curr_len, max_len = 0, 0
        
        for no in nums:
            if (no-1) not in numset:
                curr_len = 0
                while (no + curr_len) in numset:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        return max_len

"""
Time complexity: O(n)
-    All the O(n) operations are linear here. O(n)+O(n) which will result in O(n)
Space complexity: O(n)
-    Space is used by the set according to the input. If there are no duplicates which will result in the list and set to be same and worst case time complexity O(n)
"""
