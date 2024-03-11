class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq = 0
        for no in nums:
            uniq ^= no
        return uniq
        
"""
The solution works by the principle of XOR operation. Below is a detailed explanation of how it works.

Sure, let's walk through the example `[4, 1, 2, 1, 2]`:

1. Initially, `uniq` is set to 0.

2. The loop begins:
   - `uniq ^= 4`: `uniq` XOR 4 results in `uniq = 0 ^ 4 = 4`.
   
3. Next iteration:
   - `uniq ^= 1`: `uniq` XOR 1 results in `uniq = 4 ^ 1 = 5`.
   
4. Next iteration:
   - `uniq ^= 2`: `uniq` XOR 2 results in `uniq = 5 ^ 2 = 7`.
   
5. Next iteration:
   - `uniq ^= 1`: `uniq` XOR 1 results in `uniq = 7 ^ 1 = 6`.
   
6. Final iteration:
   - `uniq ^= 2`: `uniq` XOR 2 results in `uniq = 6 ^ 2 = 4`.

After iterating through all the numbers in the list, the value of `uniq` is `4`. This is because XORing all the numbers together effectively cancels out the duplicates, leaving only the single number, which is `4`. So, the function returns `4` as the result.

Time Complexity O(n)
Space Complexity O(1)
"""
