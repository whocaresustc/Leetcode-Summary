
#  314. Binary Tree Vertical Order Traversal

# BFS
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mapping = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        res = []

        while queue:
            node, x, y = queue.popleft()
            mapping[x].append((y, node.val))
            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        for i in sorted(mapping.keys()):
            res.append([val for row, val in sorted(mapping[i])])

        return res