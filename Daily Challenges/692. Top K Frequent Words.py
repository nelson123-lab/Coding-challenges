class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}

        # Creating a frequencey dictionary
        for i in words:
            d[i] = d.setdefault(i, 0) + 1

        # Sorting the dictionary according to the frequencies and then according to the words.
        d = dict(sorted(d.items(), key = lambda x: (-x[1], x[0])))

        # returning the output as list.
        keys = list(d.keys())
        return keys[:k]

"""
- Here we are using .setdefault() method of dictionary. It checks whether the i value exists in the dictionary if it is not present "i" value is added as a key and the default value is added as the value. 
- Then we will get the dictionary with frequencies but we need to sort it according to the frequencies. and then with the words.
Time Complexity O(nlogn)
Space Complexity O(n)
"""
