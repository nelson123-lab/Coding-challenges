class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate) 
        R, D = deque(), deque()

        for idx, ele in enumerate(senate):
            if ele == "R":
                R.append(idx)
            else:
                D.append(idx)
        
        while R and D:
            rTurn = R.popleft()
            dTurn = D.popleft()

            if rTurn < dTurn:
                R.append(dTurn + len(senate))
            else:
                D.append(rTurn + len(senate))
        return "Radiant" if R else "Dire"

"""
Here we are using two queue to keep track of the Radiant and Dire according to order. 
Here the usage of queue is used to improve the time complexity. Queue provides popleft() O(1) operation.

Time Complexity O(n)
- The iteration will only happend till the end of the length of the array.
Space Complexity O(n)
- The maximum each of these queues can grow is only till the input length. Both the queue will be a linear operation.
"""
