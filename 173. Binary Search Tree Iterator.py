# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inorderTraversal(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        tempNode = self.stack.pop()
        self.inorderTraversal(tempNode.right)
        return tempNode.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """

        return self.stack

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        while root:
            self.stack.append(root)
            root = root.left