# https://leetcode-cn.com/problems/container-with-most-water/


class Solution:
    # 超时
    # def maxArea(self, height: list) -> int:
    #     _max = 0
    #     for i in range(len(height) - 1):
    #         for j in range(1, len(height)):
    #             t = (j-i) * min(height[i], height[j])
    #             _max = max(_max, t)
    #     return _max

    # 两端夹逼法
    def maxArea(self, height: list) -> int:
        _max = 0
        left = 0
        right = len(height) - 1
        while left != right:
            if height[left] > height[right]:
                area = height[right] * (right-left)
                right -= 1
            else:
                area = height[left] * (right-left)
                left += 1
            _max = max(area, _max)
        return _max


height = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(height)
