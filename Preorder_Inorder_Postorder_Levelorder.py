# Preorder
# Solution 1:
def preorderTraversal(self, root):
    if root is None:
        return []
    stack = [root]  # LIFO
    preorder = []
    while stack:
        node = stack.pop()  #
        preorder.append(node.val)
        if node.right:  # node.right first for later popout
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return preorder


# Solutino 2:
    class Solution:
        def preorderTraversal(self, root: TreeNode) -> List[int]:
            p, stack = root, []
            res = []
            while p or stack:
                while p:
                    stack.append(p)
                    res.append(p.val)
                    p = p.left
                p = stack.pop()
                p = p.right
            return res

# Solution 3: Recursion
    class Solution:
        def preorderTraversal(self, root):
            res = []
            self.dfs(root, res)
            return res

        def dfs(self, root, res):
            if root:
                res.append(root.val)
                self.dfs(root.left, res)
                self.dfs(root.right, res)



# Inorder
# Solution 1:
    class Solution:
        def inorderTraversal(self, root: TreeNode) -> List[int]:
            p, stack = root, []
            res = []
            while p or stack:
                while p:
                    stack.append(p)
                    p = p.left
                p = stack.pop()
                res.append(p.val)  # res append operation different with preorder traversal
                p = p.right
            return res


# Solution 2:
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)


# Postorder : left -> right -> root
# Method 1:  Reverse modified preorder traversal: root -> left -> right  Time O(N) Space O(h)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, inorder_modified = [root], []
        while stack:
            node = stack.pop()
            inorder_modified.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return reversed(inorder_modified)


# Mark with visited or not
# Time: O(N), Space: O(h)
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        postorder, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    postorder.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return postorder

# Level order traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = collections.deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)

        return levels