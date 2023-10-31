class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [ xor(0 if i==0 else pref[i-1],  n)  for i,n in enumerate(pref)]
