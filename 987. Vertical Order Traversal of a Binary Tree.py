
#  314. Binary Tree Vertical Order Traversal

# BFS

# Key difference with 314: If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

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

    class Solution(object):
        def verticalTraversal(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            mapping = collections.defaultdict(list)
            queue = collections.deque([(root, 0, 0)])
            res = []
            x_min = x_max = 0
            while queue:
                node, x, y = queue.popleft()
                mapping[x].append((y, node.val))
                x_min, x_max = min(x_min, x), max(x_max, x)
                if node.left:
                    queue.append((node.left, x - 1, y + 1))
                if node.right:
                    queue.append((node.right, x + 1, y + 1))

            for i in range(x_min, x_max + 1):
                res.append([val for col, val in sorted(mapping[i])])

            return res