# time O(n*n), space O(n*n)
class Solution2(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    num = board[row][col]  # str, don't change to int!
                    if (row, num) in res or (num, col) in res \
                    or (num, row//3, col//3) in res:
                        return False
                    res.add((row, num))
                    res.add((num, col))
                    res.add((num, row//3, col//3))
        return True