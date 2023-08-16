class Solution:
    def isHappy(self, n: int, visited= None) -> bool:
        if visited is None:
            visited = set()

        if n == 1:
            return True

        if n in visited:
            return False
        visited.add(n)

        new_num = sum(int(digit)**2 for digit in str(n))

        return self.isHappy(new_num, visited)


"""
Here we are checking if there is a number being repeated in between the iteration.Then we can return False as it will keep on repeating. We are using a set to keep track of the numbers.
Time Compelxity O(logn)
- It is due to the process of recurssion.
Space Complexity O(n)
- Here a set is used for keeping track of the new numbers. Where n is the number of times the recursion occurs.
"""
