class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sorting the numbers
        nums.sort()
        # Initializing distance
        distance = float('inf')
        # Iterating through the list
        for idx in range(len(nums) - 2):
            l, r = idx+1, len(nums)-1
            new_target = target - nums[idx]
            while l < r:
                two_sum = nums[l] + nums[r]
                curr_distance = new_target - two_sum
                
                if abs(distance) > abs(curr_distance):
                    distance = curr_distance
                # Checking different condition for the closest.
                if two_sum == new_target:
                    return target
                elif two_sum < new_target:
                    l += 1
                else:
                    r -= 1
        return target - distance

"""
This is similar to 3sum problem but here we need to check with distance that is minimal each for all the different combinations of 3 numbers.
Time Complexity O(n^2)
- This is due to the while loop inside the for loop that works for n times within the loop in the worst case scenario.
Space Complexity O(1)
"""
