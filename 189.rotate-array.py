# https://leetcode.com/problems/rotate-array/ 


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums[k+1:].append(nums[0:k])
