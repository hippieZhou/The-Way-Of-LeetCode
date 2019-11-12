class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(0, nums[i-1]) + nums[i]
        return max(nums)
