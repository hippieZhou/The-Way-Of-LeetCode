class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for x in nums:
            last, now = now, max(last + x, now)
        return now
