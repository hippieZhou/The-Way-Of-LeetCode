# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。


class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(2, n):
            third = first + second
            first, second = second, third
        return second


ways = Solution().climbStairs(2)
print(ways)
