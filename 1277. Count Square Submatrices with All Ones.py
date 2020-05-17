"""https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/518072/Python-O(-m*n-)-sol-by-DP-93%2B-with-Hint-and-Demo"""

# 221. Maximal Square

class Solution:
    def countSquares(self, A):
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))