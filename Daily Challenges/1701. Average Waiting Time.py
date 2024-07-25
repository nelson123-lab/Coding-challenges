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
- 
"""
