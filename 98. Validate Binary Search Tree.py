class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            # if not root:
            #     continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            if root.right:
                stack.append((root.right, val, upper))
            if root.left:
                stack.append((root.left, lower, val))
        return True


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # inorder traversal
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True