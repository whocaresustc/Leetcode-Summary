# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me


import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            for neighbor in edges[curr]:
                if neighbor == prev: continue  # this step is important: keep going foward and don't go back
                if not low[neighbor]: # if not visited
                    result += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1: # if all the neighbors lowest rank is higher than rank + 1
                    result.append([curr, neighbor])
            return result

        low, edges = [0] * n, collections.defaultdict(list) # lowest rank
        for u, v in connections: # building graph
            edges[u].append(v)
            edges[v].append(u)

        return dfs(1, 0, -1) # starting from node 0