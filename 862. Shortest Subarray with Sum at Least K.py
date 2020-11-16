# prefix sum
import heapq


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        q = [(0, -1)]
        cum = 0
        res = float('inf')
        for i, x in enumerate(A):
            cum += x

            while q and cum - q[0][
                0] >= K:  # if satisfy condition popout all the solutions(smallest first) ending with current i
                res = min(res, i - heapq.heappop(q)[1])

            heapq.heappush(q, (cum, i))
        return res if res < float('inf') else -1


def shortestSubarray(self, A, K):
    d = collections.deque([[0, 0]])
    res, cur = float('inf'), 0
    for i, a in enumerate(A):
        cur += a
        while d and cur - d[0][1] >= K:
            res = min(res, i + 1 - d.popleft()[0])
        while d and cur <= d[-1][1]:
            d.pop()
        d.append([i + 1, cur])
    return res if res < float('inf') else -1