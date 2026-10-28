class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        max_sum = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            pair_sum = nums[left] + nums[right]
            max_sum = max(max_sum, pair_sum)
            left += 1
            right -= 1
        return max_sum