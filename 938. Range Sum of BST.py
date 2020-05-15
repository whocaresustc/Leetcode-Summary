class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                ans += node.val
            if node.right and node.val < R:
                stack.append(node.right)
            if node.left and node.val > L:
                stack.append(node.left)

        return ans