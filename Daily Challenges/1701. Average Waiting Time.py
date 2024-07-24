class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        curTime = 0
        totalTime = 0
        for i in range(n):
            if curTime <= customers[i][0]:
                totalTime += customers[i][1]
                curTime = customers[i][0] + customers[i][1]
            else:
                totalTime += (curTime - customers[i][0] + customers[i][1])
                curTime += customers[i][1]
        return totalTime / n
