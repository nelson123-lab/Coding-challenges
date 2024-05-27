class Solution:
    def dailyTemperatures(self, temps):
        results = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                index = stack.pop()
                results[index] = i - index
            stack.append(i)

        return results
"""
- Here we use a stack to find the daily temperature increase. 

Time Complexity O(n)
Space Complexity O(n)
"""
