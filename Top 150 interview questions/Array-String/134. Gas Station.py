class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i+1
        return start 

"""
- This is a greedy approach. Here we check whether the total cost of gas for travel is greater than the gas available at the station in total. If this is 
not available, then there is no starting position.
- The next step we are doing is adding up the remaining gas after each station. If the gas becomes negative we start from the next index. 
- We don't need to worry about getting index out of range. There will be a solution before that or it will be the last index. 

Time Complexity O(1)
Space Complexity O(1)
"""
