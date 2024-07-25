class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        t, total = 0, 0

        for arrival, order in customers:
            if t > arrival:
                total += t - arrival
            else:
                t = arrival
            total += order
            t += order
        return total/float(len(customers))


"""
- Here we can consider this problem as an interval problem. Since the start of the interval is already sorted.
- We need a variable to keep track of the current time.
Time Complexity O(n)
Space Complexity O(1)
"""
