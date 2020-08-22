# Reverse level order traversal
# Similar to 102 Binary Tree Level Order Traversal


from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    ans.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ans


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        ans = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level == len(ans):
                ans.append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return ans


