# 颠倒给定的 32 位无符号整数的二进制位。


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2::].zfill(32)[::-1], 2)


result = Solution().reverseBits(92)
print(result)
