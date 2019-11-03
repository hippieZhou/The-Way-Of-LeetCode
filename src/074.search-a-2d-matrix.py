class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix(self, matrix: list, target: int) -> bool:
        if matrix == [[]]:
            return False
        array = [[0, 0]] * len(matrix)
        for i, val in enumerate(matrix):
            array[i] = [val[0], val[len(val) - 1]]
        for i, val in enumerate(array):
            if target >= val[0] and target <= val[1]:
                return target in matrix[i]
