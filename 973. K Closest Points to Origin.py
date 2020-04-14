# O(NlgK)   O(k)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x * x + y * y)  # remaining is the ans
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]


# klg(N) O(N)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [((x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(heap)
        ans = [0] * K
        for i in range(K):
            ans[i] = heapq.heappop(heap)[1::]
        return ans