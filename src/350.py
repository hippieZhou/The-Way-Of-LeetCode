# 给定两个数组，编写一个函数来计算它们的交集。


class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        inter = set(nums1) & set(nums2)
        print(inter)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
            print(l)
        return l


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
li = Solution().intersect(nums1, nums2)
print(li)
