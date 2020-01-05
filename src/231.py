# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。


class Solution:
    def isPowerOfTwo(self, n):
        x = 0
        while 2**x < n:
            x = x + 1
        return 2 ** x == n


# print(2**1)
# print(2**2)
# print(2**3)
# print(2**4)

b = Solution().isPowerOfTwo(16)
print(b)
