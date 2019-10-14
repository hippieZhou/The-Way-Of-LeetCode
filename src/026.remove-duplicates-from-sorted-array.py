# https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 

class Solution:
    # 解法一：逆序遍历，防止移动大量元素
    # def removeDuplicates(self, nums: list) -> int:
    #     if nums is None:
    #         return 0

    #     for i in range(len(nums)-1, 0, -1):
    #         if nums[i] == nums[i-1]:
    #             nums.pop(i)
    #     return len(nums)

    # 解法二
    def removeDuplicates(self, nums: list) -> int:
        if nums is None:
            return 0

        id = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[id]:
                nums[id+1] = nums[i]
                id += 1
        return id + 1


for i in range(1, 0):
    print(i)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
