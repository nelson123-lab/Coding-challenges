class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref: Dict[Tuple[int], List[str]] = {}

        for s in strs:
            count = [0] * 26

            for chr in s:
                count[ord(chr) - ord('a')] += 1
            
            count_tuple = tuple(count)
            if count_tuple not in ref:
                ref[count_tuple] = [s]
            else:
                ref[count_tuple].append(s)
        
        return list(ref.values())

"""
- Here we are keeping a ref hashmap to keep track of all string character count so that all the strings with similar character count gets grouped together.
- This solution is more efficient than sorting in terms of time Complexity.
Time COmplexity O(m*n) - m*n is the total number of characters in the input string.
Space Complexity O(m*n)
"""
