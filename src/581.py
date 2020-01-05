# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 你找到的子数组应是最短的，请输出它的长度。


class Solution(object):
    def findUnsortedSubarray(self, nums: list) ->int:
        temp = nums[:]
        temp.sort()
        i, j = 0, len(temp) - 1
        while i < len(nums) and nums[i] == temp[i]:
            i += 1

        while j > i+1 and nums[j] == temp[j]:
            j -= 1

        return j-i + 1


n = Solution().findUnsortedSubarray([2,1])
print(n)
