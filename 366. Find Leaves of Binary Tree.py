# DFS

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):  # return the depth of node and add the res
        if not node:
            return 0
        depth = max(self.dfs(node.left, res), self.dfs(node.right, res)) + 1
        if len(res) < depth:
            res.append([])
        res[depth - 1].append(node.val)
        return depth
    