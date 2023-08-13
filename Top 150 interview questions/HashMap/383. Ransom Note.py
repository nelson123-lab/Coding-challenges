class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) >= Counter(ransomNote)

"""
Time Complexity O(m+n)
- Solution works in O(m+n) time complexity where m and n are the length of first and the second array
Space Complexity O(m+n)
- Here the space used to store the elements inside the counter is of similar size.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Creating a counter with the frequencies of the occurances of the elements within the magazine.
        hmap_mag = Counter(magazine)
        for i in ransomNote:
            if i in hmap_mag and hmap_mag[i] > 0:
                # Decreases the frequency count when the elements are present in the hashmap.
                hmap_mag[i] -= 1
            # If the element is not present in the magazine it return False directly, the magazine won't be able to make the ransomNote.
            else:
                return False
        # If there exists some frequencies within magazine it won't matter. The creation of ransomNote is possible.
        return True

"""
Time Complexity O(m)
- Here only 1 iteration is happening through the ransomNote. Here m is the length of the magazine string. It is greater than ransomNote so O(m+n) becomes O(m).
Space Complexity O(m)
- Here a hashmap is generated with the elements of the magazine. Here m is length of the elements in the magazine.
"""
