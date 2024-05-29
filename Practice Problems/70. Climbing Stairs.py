"""
Recursive solution:
- Here it divides the number of stairs into a tree format. 
- No of ways we can climb 3 steps = no of ways we can climb 2 stairs + no of ways we can climb 1 stairs.
- We will define the no of ways it is required to climb 1 step and 2 steps as the base cases.
Time complexity O(2^n)
Space Complexity O(n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

"""
Dynamic Programming solution
- This works like a Fibonacci series removing the usage of redundant function calls in recursion.
Time complexity O(n)
Space compelxity O(1)
"""
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1

        one_before = 1
        two_before = 1
        total = 0

        for i in range(n-1):
            total = one_before + two_before
            two_before = one_before
            one_before = total

        return total
