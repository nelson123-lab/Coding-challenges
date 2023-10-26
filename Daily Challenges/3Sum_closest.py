class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input array in ascending order.
        closest_sum = float('inf')  # Initialize closest_sum with positive infinity.

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Pointers for the remaining subarray.
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the current sum is closer to the target than the previous closest sum,
                # update closest_sum.
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1  # Move the left pointer to increase the sum.
                else:
                    right -= 1  # Move the right pointer to decrease the sum.

        return closest_sum
        
