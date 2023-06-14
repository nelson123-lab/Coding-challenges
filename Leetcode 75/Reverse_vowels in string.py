class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s_list = list(s)
        vowels = ['a', 'e','i','o','u']
        while l<r:
            if s_list[l].lower() not in vowels:
                l += 1
            if s_list[r].lower() not in vowels:
                r -= 1
            if s_list[l].lower() in vowels and s_list[r].lower() in vowels:
                temp = s_list[l]
                s_list[l] = s_list[r]
                s_list[r] = temp
                l += 1
                r -= 1
        return "".join(s_list)