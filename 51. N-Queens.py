# O(N!) O(N)
class Solution:
    def solveNQueens(self, n):
        """
        :param n:
        :return:
        """
        res = []

        def dfs(queens, ddiff, ssum):  # each row place one queen: represented by index col
            p = len(queens)  # index of row
            # if p == n: then it is a solution
            if p == n:
                queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]  # i: index column in each row
                res.append(queens)
                return
            for q in range(n):  # index of column
                if q in queens or p - q in ddiff or p + q in ssum:
                    continue
                dfs(queens + [q], ddiff + [p - q], ssum + [p + q])

        dfs([], [], [])
        return res
