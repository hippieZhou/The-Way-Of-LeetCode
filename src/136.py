# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 示例 2:

# 输入: [4,1,2,1,2]
# 输出: 4


class Solution:
    def singleNumber(self, nums: list) ->int:
        from functools import reduce
        return reduce(int.__xor__, nums)

        # num = None
        # for x in nums:
        #     if nums.count(x) == 1:
        #         num = x
        #         break
        # return num


print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
