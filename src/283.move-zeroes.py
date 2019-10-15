# https://leetcode-cn.com/problems/move-zeroes/


class Solution:
    # def moveZeroes(self, nums: list) -> None:
    #     for i, v in enumerate(nums):
    #         if v == 0:
    #             nums.remove(0)
    #             nums.append(0)

    # def moveZeroes(self, nums: list) -> None:
    #     i = 0  # 记录非 0 元素对应的下标
    #     for j in range(len(nums)):
    #         if nums[j] != 0:
    #             nums[i] = nums[j]
    #             if j != i:
    #                 nums[j] = 0
    #             i += 1

    def moveZeroes(self, nums: list) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
