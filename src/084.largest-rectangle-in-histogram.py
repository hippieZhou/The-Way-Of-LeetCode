class Solution:
    # def largestRectangleArea(self, heights: list) -> int:
    #     res = 0
    #     for i in range(len(heights)):
    #         left_i = right_i = i
    #         while left_i >= 0 and heights[left_i] >= heights[i]:
    #             left_i -= i
    #         while right_i < len(heights) and heights[right_i] >= heights[i]:
    #             right_i += 1
    #         res = max(res, (right_i - left_i - 1) * heights[i])
    #     return res

    def largestRectangleArea(self, heights: list) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            heights.pop()
            return ans
