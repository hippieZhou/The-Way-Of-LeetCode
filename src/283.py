# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: list) ->None:
        nums.sort(key=bool, reverse=True)


l = [0, 1, 0, 3, 12]
Solution().moveZeroes(l)
print(l)
