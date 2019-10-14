# https://leetcode.com/problems/climbing-stairs/


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     array = [1, 2]
    #     for i in range(2, n+1):
    #         array.append(array[i-1] + array[i-2])
    #     return array[n-1]

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b, c = 1, 2, 3
        for i in range(3, n+1):
            c, = a+b
            a, b = b, c
        return c


print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
