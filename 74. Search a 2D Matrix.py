# Binary search
# O(lg(m*n)) O(1)
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        start, end = 0, n * m - 1
        while start <= end:
            mid = (start + end) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

