# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。


class Solution:
    def productExceptSelf(self, nums: list) -> list:
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res

        # sets = []
        # for x in nums:
        #     index = nums.index(x)
        #     val = 1
        #     for i, x in enumerate(nums):
        #         if i == index:
        #             continue
        #         else:
        #             val = val * x
        #     sets.append(val)
        # return sets


array = Solution().productExceptSelf([1, 2, 3, 4])
print(array)
