# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:

# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        return sorted(nums)[-k]


num = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(num)
