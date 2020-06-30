from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        res = []
        level_number = 0
        while stack:
            level = []
            level_number += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                level.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            if level_number % 2 == 1:
                level = list(reversed(level))

            res.append(level)

        return res