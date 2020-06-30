# DFS with recursion
# Time O(N)
# Space worst O(N) best O(log(N))

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return self.dfs(root, str(root.val), [])

    def dfs(self, node, path, res):
        if node.left is None and node.right is None:
            res.append(path)
        if node.left:
            self.dfs(node.left, path + "->" + str(node.left.val), res)
        if node.right:
            self.dfs(node.right, path + "->" + str(node.right.val), res)

        return res

# DFS with iteration
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

        return res


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def dfs(root, cur):
            if not root:
                return
            if not root.left and not root.right:
                self.res.append(cur + str(root.val))
            if root.left:
                dfs(root.left, cur + str(root.val) + "->")
            if root.right:
                dfs(root.right, cur + str(root.val) + "->")

        dfs(root, "")
        return self.res