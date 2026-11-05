class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first binary search the rows to figure out which row its on
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        targetRow = r
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[targetRow][m] == target:
                return True
            elif matrix[targetRow][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False