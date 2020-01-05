# 给定一个没有重复数字的序列，返回其所有可能的全排列。


class Solution:
    def permute(self, nums: list) -> list:
        from itertools import permutations
        return list(permutations(nums))


result = Solution().permute([1, 2, 3])
print(result)
