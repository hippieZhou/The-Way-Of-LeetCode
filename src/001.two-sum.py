# https://leetcode-cn.com/problems/two-sum/


class Solution:
    # def twoSum(self, nums: list, target: int) -> list:
    #     for i, v in enumerate(nums[:len(nums) - 1]):
    #         if nums[i+1:].count(target-v) == 0:
    #             return [i, i + 1 + nums[i+1:].index(target-v)]

    def twoSum(self, nums: list, target: int) -> list:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic:
                return [i, dic[v]]
            dic[target-v] = i


v = Solution().twoSum([3, 2, 4], 6)
print(v)
