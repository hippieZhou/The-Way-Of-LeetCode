class Solution:
    def subsets(self, nums: list) -> list:
        subs = [[]]
        for num in nums:
            subs += [[num] + i for i in subs]
        return subs


v = Solution().subsets([1, 2, 3])
print(v)
