# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: true


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))


v = Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(v)
