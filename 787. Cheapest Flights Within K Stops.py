# https://leetcode.com/problems/cheapest-flights-within-k-stops/solution/

# Method 1: shortest path problem on a weighted graph
"""a standard rule of thumb that is followed for solving shortest path problems is that we mostly use Breadth-first search for unweighted graphs and use Dijkstra's algorithm for weighted graphs. """

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for edge in flights:
            s, d, cost = edge
            graph[s].append([d, cost])

        queue = [(0, 0, src)]

        while queue:
            cost, dist, current = heapq.heappop(queue)

            if current == dst:
                return cost
            for nei, c in graph[current]:
                if dist <= K:
                    heapq.heappush(queue, (cost + c, dist + 1, nei))
        return -1


# Method 2:  DFS + memo
class Solution:
    def findShortest(self, node, stops, dst, n):
        if node == dst:
            return 0

        if stops < 0:
            return float("inf")

        if (node, stops) in self.memo:
            return self.memo[(node, stops)]

        # Recursive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:  # if existing
                ans = min(ans, self.findShortest(neighbor, stops - 1, dst, n) + self.adj_matrix[node][neighbor])

        # Cache the result
        self.memo[(node, stops)] = ans
        return ans

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w

        result = self.findShortest(src, K, dst, n)
        return -1 if result == float("inf") else result


# BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w

        # Shortest distances dictionary
        distances = {}
        distances[(src, 0)] = 0

        # BFS Queue
        queue = deque([src])

        # Number of stops taken
        stops = 0
        ans = float("inf")

        # Iterate until we exhaust K+1 levels or the queue gets empty
        while queue and stops < K + 1:

            # Iterate on current level
            for _ in range(len(queue)):
                node = queue.popleft()
                # Loop over neighbors of popped node
                for nei in range(n):
                    if adj_matrix[node][nei] > 0:
                        dU = distances.get((node, stops), float("inf"))
                        dV = distances.get((nei, stops + 1), float("inf"))
                        wUV = adj_matrix[node][nei]

                        # No need to update the minimum cost if we have already exhausted our K stops: we can skip this checking
                        if stops == K and nei != dst:
                            continue

                        if dU + wUV < dV:
                            distances[nei, stops + 1] = dU + wUV
                            queue.append(nei)

                            # Shortest distance of the destination from the source
                            if nei == dst:
                                ans = min(ans, dU + wUV)
            stops += 1

        return -1 if ans == float("inf") else ans