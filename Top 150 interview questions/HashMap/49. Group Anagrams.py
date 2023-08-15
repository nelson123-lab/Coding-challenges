class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            hashmap[sorted_word].append(word)

        return list(hashmap.values())

"""
Defaultdict is used to get rid of the key error. Hashmap can also be used here.

TIme Complexitiy O(m * nlog n)
- Here the O(n) time complexity is required for iteration through the string. The words are sorted within in the loop which takes around O(nlogn) time complexity. Therefore resulting in a O(m*nlogn) time complexity.
Space Complexity O(m*k)
- It depends on the input. Here the hashmap is used to store multiple words. The storage depends on the unique elements. The space complexity can be lowered upto O(n) as well.
"""
