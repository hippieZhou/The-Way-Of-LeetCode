class Solution:
    # def maxSlidingWindow(self, nums: list, k: int) -> list:
    #     res = []
    #     if nums != []:
    #         for i in range(0, len(nums) - k+1):
    #             res.append(max(nums[i:i+k]))
    #     return res

    def maxSlidingWindow(self, nums: list, k: int) -> list:
        return [] if len(nums) == 0 else [max(nums[i:i+k] for i in range(0, len(nums) - k + 1))]


v = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(v)
