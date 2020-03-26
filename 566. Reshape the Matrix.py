# O(m * n) O(m * n)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if r * c != m * n or not nums:
            return nums
        ans = [[]]
        p1, p2, q1, q2 = 0, 0, 0, 0
        for _ in range(r * c):
            if p2 == c:
                ans.append([])
                p2 = 0
                p1 += 1
            if q2 == n:
                q2 = 0
                q1 += 1
            ans[p1].append(nums[q1][q2])
            p2 += 1
            q2 += 1
        return ans


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [[0] * c for _ in range(r)]
        m, n = len(nums), len(nums[0])
        if r * c != m * n or not nums:
            return nums
        rows, cols = 0, 0
        for i in range(m):
            for j in range(n):
                ans[rows][cols] = nums[i][j]
                cols += 1
                if cols == c:
                    rows += 1
                    cols = 0
        return ans