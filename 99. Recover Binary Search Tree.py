class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.inorder(root, nodes)
        if len(nodes) < 2:
            return
        vals = [node.val for node in nodes]
        vals.sort()
        for i, node in enumerate(nodes):
            node.val = vals[i]

    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)