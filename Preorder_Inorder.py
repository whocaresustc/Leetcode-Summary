# Preorder
# Solution 1:
def preorderTraversal(self, root):
    if root is None:
        return []
    stack = [root]  # can we use deque([]) here, the answer is yes!
    preorder = []
    while stack:
        node = stack.pop()  # last in first out
        preorder.append(node.val)
        if node.right:  # that is why appending node.right first
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




# Inorder
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


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.results.append(root.val)
        self.traverse(root.right)