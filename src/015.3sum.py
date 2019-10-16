# https://leetcode.com/problems/3sum/


class Solution:
    # def threeSum(self, nums: list) -> list:
    #     nums.sort()
    #     array = set()
    #     for i in range(len(nums) - 2):
    #         for j in range(i+1, len(nums) - 1):
    #             for k in range(j+1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     array.add((nums[i], nums[j], nums[k]))
    #     return array

    def threeSum(self, nums: list) -> list:
        nums.sort()
        array = []
        for i in range(len(nums) - 2):
            # 元素相同则过滤
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s > 0:
                    left += 1
                else:
                    array.append([i, left, right])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return array
