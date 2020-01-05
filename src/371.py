# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a.__add__(b)

        # return sum([a,b])
        # return a + + b


print(Solution().getSum(1, 2))
print(Solution().getSum(-2, 3))
