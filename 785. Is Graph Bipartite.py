# nodes for each edge in two different colors
# BFS for every node

"""DFS is usually implemented with recursive calls but we can implement it iteratively using stack mimicking the function call stack."""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = collections.deque([node])
                color[node] = 0
                while queue:
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei not in color:
                            queue.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True