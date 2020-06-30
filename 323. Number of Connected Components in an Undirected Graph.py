class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        ranks = [1] * n

        def find(x):
            if x == parents[x]:
                return x
            return find(parents[x])

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if ranks[root_x] < ranks[root_y]:
                root_x, root_y = root_y, root_x
            parents[root_y] = root_x
            ranks[root_x] += 1

        for u, v in edges:
            union(u, v)

        # map(union, edges)

        return len({find(x) for x in parents})