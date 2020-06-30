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