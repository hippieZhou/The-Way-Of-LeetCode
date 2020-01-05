# 给定 nums = [0,0,1,1,1,2,2,3,3,4],

# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

# 你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeDuplicates(self, nums: list)->int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1 if nums else 0


nums = [1, 1, 2]
sum = Solution().removeDuplicates(nums)
print(nums)
print(sum)
