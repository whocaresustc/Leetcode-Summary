# Topological sort
# O(2*E + V) O(2*E + V)
# BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = collections.defaultdict(list)

        for prerequisite in prerequisites:
            neighbors[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = collections.deque(node for node in range(numCourses) if indegree[node] == 0)
        remain = numCourses

        while queue:
            node = queue.popleft()
            remain -= 1
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return remain == 0

# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = collections.defaultdict(list)

        for prerequisite in prerequisites:
            neighbors[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        stack = [node for node in range(numCourses) if indegree[node] == 0]
        remain = numCourses

        while stack:
            node = stack.pop()
            remain -= 1
            for neighbor in neighbors[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
        return remain == 0