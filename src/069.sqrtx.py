class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left < right:
            mid = left + (right-left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    # 牛顿迭代法
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r * r > x:
    #         r = (r + x/r) / 2
    #     return r
