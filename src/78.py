# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。


class Solution(object):
    def subsets(self, nums: list):
        from itertools import combinations
        return sum([list(combinations(nums, i)) for i in range(len(nums) + 1)], [])


sets = Solution().subsets([1, 2, 3])
print(sets)
