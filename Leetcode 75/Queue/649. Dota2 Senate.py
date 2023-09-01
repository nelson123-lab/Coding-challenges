class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        votes = {"D":1, "R":-1}
        count = 0
        while abs(count) < len(q):
            v = q.popleft()
            count += votes[v]            
            if count > 0 and v == "D" or count<0 and v == "R":
                q.append(v)     
        return 'Dire' if count>0 else  'Radiant'
