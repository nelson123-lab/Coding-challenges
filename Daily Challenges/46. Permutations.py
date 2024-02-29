class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]  # Base case

        ap = []  # List to store the permutations

        for i in range(len(nums)):
            ce = nums[i]
            re = nums[:i] + nums[i+1:]

            for permutation in self.permute(re):
                ap.append([ce] + permutation)

        return ap

"""
- This works through recurssion. We can even use the itertools permutation method to solve this problem but dosen't actually solve the question. The purpose is to to it manually.
- The logic works in a way that it takes each element and creates different permutations of remaining elements and combines them.
eg: Out target is to find all permuations of [1, 2, 3]
- The program first takes 1 and makes a list of permutation with the rest of the elements and combines to get the 
                [[2, 3], [3, 2]]
                [1] + [2, 3] 
                [1] + [3, 2]
                - [[1, 2, 3], [1, 3, 2]]
                [[1, 3], [3, 1]]
                [2] + [1, 3] 
                [2] + [3, 1]
                - [[2, 1, 3], [2, 3, 1]]
                [[1, 2], [2, 1]]
                [3] + [1, 2] 
                [3] + [2, 1]
                - [[3, 1, 2], [3, 2, 1]]

Time Complexity: O(n!)
Space Complexity: O(n!)
"""
