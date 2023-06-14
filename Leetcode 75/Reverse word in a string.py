class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        l,r = 0, len(s_list)-1
        reversed_list = s_list[::-1]
        while l<r:
            if reversed_list[l] == " ":
                reversed_list.remove(reversed_list[l])
                l += 1
            if reversed_list[r] == " ":
                reversed_list.remove(reversed_list[r])
                r -= 1
        return " ".join(reversed_list)

ans = Solution()
print(ans.reverseWords("the sky is  blue"))
