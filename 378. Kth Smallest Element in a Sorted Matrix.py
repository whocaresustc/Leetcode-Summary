# heapq
# O(k*logn) O(k)
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = [(row[0], 0, i) for i, row in enumerate(matrix)]
        n = len(matrix[0])
        heapq.heapify(minHeap)
        for _ in range(k):
            num, index, row = heapq.heappop(minHeap)
            if index < n - 1:
                heapq.heappush(minHeap, (matrix[row][index + 1], index + 1, row))
        return num


# Binary search
# O(n∗lg(hi−lo))  O(1)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        n = len(matrix[0]) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.check(matrix, mid, n) < k:
                lo = mid + 1
            else:
                hi = mid  # not mid - 1 since mid could be the answer
        return lo  # or hi (lo = hi = mid)

    def check(self, matrix, mid, j):  # how many elements in the matrix is smaller or equal to mid
        count = 0
        for i in range(len(matrix)):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += j + 1
        return count