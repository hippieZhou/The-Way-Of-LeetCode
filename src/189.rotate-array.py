# https://leetcode.com/problems/rotate-array/


class Solution:
    # def rotate(self, nums: list, k: int) -> None:
    #     while k:
    #         nums.insert(0, nums.pop())
    #         k -= 1

    # def rotate(self, nums: list, k: int) -> None:
    #     k %= len(nums)
    #     nums[:] = nums[::-1]
    #     nums[:] = nums[:k][::-1] + nums[k:][-1]

    def rotate(self, nums: list, k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
