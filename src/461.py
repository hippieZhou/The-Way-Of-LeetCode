# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

# 给出两个整数 x 和 y，计算它们之间的汉明距离。

# 注意：
# 0 ≤ x, y < 231.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


print(1^2)
n = Solution().hammingDistance(1, 4)
print(n)
