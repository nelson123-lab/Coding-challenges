class Solution(object):
    def canJump(self, nums):
        curr = nums[0]
        for i in range(1,len(nums)):
            if curr == 0:
                return False
            curr -= 1
            curr = max(curr, nums[i])     
        return True

"""
The overall idea here is that if the first element of the array is 0 we can't jump to any other array and it will directly return False.
It keeps track of the maximum number of steps that can be taken from the current position using the curr variable.
Time Complexity O(n)
Space Complextiy O(1)
"""

# A DP Approach


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i]>=goal):
                #it is possible to reach to the goal...
                goal=i
        return goal==0

"""
The time complexity of this program is O(n), where n is the length of the input list `nums`. This is because the program iterates through the list once 
in the `for` loop, checking each element to determine if it can reach the goal. The loop runs in reverse order, starting from the second-to-last element and ending at the first element, so it visits each element once.

The space complexity of this program is O(1), which means it uses constant space. This is because the program only uses a fixed amount 
of additional space to store the `goal` variable and the loop index `i`. The space used does not depend on the size of the input list `nums`.
"""
