class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Converting the string to a list inorder to do list operations
        senate = list(senate)

        # Making two queue for keeping track of Indices of both Radiant and Dire
        R = deque()
        D = deque()

        # Appending the indieces of both Radiant and Dire into there respective queues
        # This is done to keep track of the order in which they appear. The Initially appeared Radiant can remove the power of later appreared Dire. 
        # "RDD" here R removes the power of D and the later appeared D removes the power of R. Thus we should return D.
        for idx, ele in enumerate(senate):
            if ele == "R":
                R.append(idx)
            else:
                D.append(idx)
        
        # Checking if both R and D exists.
        while R and D:
            # Taking the first elements and comparing with each other to check which one came first.
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
