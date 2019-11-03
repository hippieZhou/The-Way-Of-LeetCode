class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(sorted(nums))

    def findMin(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid-1

    def findMin(self, nums: list) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if high - low <= 1:
                return min(nums[high], nums[low])
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid-1
