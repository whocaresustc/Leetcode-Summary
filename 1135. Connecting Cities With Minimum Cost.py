# Union Find with path compression and union by ranking
# O(N log N) O(N)

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        parents = list(range(N))
        ranks = [1] * N

        def find(x):
            if x == parents[x]:
                return x
            return find(parents[x])

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False
            if ranks[root_u] < ranks[root_v]:  # compare ranking of their roots
                root_u, root_v = root_v, root_u
            parents[root_v] = root_u
            ranks[root_u] += 1
            return True

        connections.sort(key=lambda x: x[2])
        ans = 0
        for u, v, cost in connections:
            if union(u - 1, v - 1):
                ans += cost

        groups = len(set(find(x) for x in parents))
        return ans if groups == 1 else -1