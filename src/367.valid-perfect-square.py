class Solution:
    def isPerfectSquare(self, nums: int) -> bool:
        left = 1
        while left * left <= nums:
            if left * left == nums:
                return True
            left += 1
        return False

    def isPerfectSquare(self, num: int) -> bool:
        ans = num
        while ans * ans > num:
            ans = (ans + num / ans) // 2
        return ans * ans == num

    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            ans = mid * mid
            if ans == num:
                return True
            elif ans > num:
                right = mid - 1
            elif ans < num:
                left = mid + 1
        return False
