# Recursion
# O(H) O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:  # on both sides
            return root
        elif left:  # on left side
            return left
        else:  # on right side
            return right

# Iteration: Store all nodes' parents using dict and then traverse back to find the lowest ancestors
# O(H) O(H)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent: # DFS search unitl finding both
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
