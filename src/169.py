# 组中出现次数大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在众数。

# 示例 1:

# 输入: [3,2,3]
# 输出: 3
# 示例 2:

# 输入: [2,2,1,1,1,2,2]
# 输出: 2


class Solution:
    def maiorityElement(self, nums: list) -> int:
        return sorted(nums)[len(nums)//2]


v = Solution().maiorityElement([2, 2, 1, 1, 1, 2, 2])
print(v)
