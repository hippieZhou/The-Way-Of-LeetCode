# https://leetcode-cn.com/problems/container-with-most-water/


class Solution:
    # 超时
    def maxArea(self, height: list) -> int:
        _max = 0
        for i in range(len(height) - 1):
            for j in range(1, len(height)):
                t = (j-i) * min(height[i], height[j])
                max = max(_max, t)
        return _max

    # 两端夹逼法
    def maxArea(self, height: list) -> int:
        pass
