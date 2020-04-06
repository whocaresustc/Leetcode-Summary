class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self, p):
        self.parent[p] = p
        self.rank[p] = 1
        self.count += 1

    def find(self, x):
        if self.parent[x] == x:  # path compression
            return x
        return self.find(self.parent[x])

    def union(self, a, b):  # union with rank: with rules so that path compression can be realized
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                root_a, root_b = root_b, root_a
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
            self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        islands = UnionFind()
        for p in map(tuple, positions):
            if p in islands.parent:
                ans += [islands.count]
            else:
                islands.add(p)
                for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                    q = (p[0] + dp[0], p[1] + dp[1])
                    if q in islands.parent:
                        islands.union(p, q)
                ans += [islands.count]
        return ans