# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    def twoSum(self, nums: list, target: int)-> list:
        for x in range(len(nums)):
            num = target - nums[x]
            if num in nums[x+1:]:
                return [x, nums.index(num, x+1)]
        return []


nums = [3, 3]
target = 6

result = Solution().twoSum(nums, target)
print(result)
