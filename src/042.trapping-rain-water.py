# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    # def trap(self, height: list) -> int:
    #     ans = 0
    #     h1, h2 = 0, 0
    #     for i in range(len(height)):
    #         h1 = max(h1, height[i])
    #         h2 = max(h2, height[-i-1])
    #         ans = ans + h1 + h2 - height[i]
    #     return ans - len(height) * h1

    def trap(self, height: list) -> int:
        ans = 0
        if height == [] or len(height) < 3:
            return ans
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans


array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
v = Solution().trap(array)
print(v)
