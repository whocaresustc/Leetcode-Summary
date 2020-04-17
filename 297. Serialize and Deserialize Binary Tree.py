class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if node is None:
                res.append("None")
            else:  # preorder traversal
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)

        res = []  # global variable for the helper function
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(data):
            val = next(data)
            if val == 'None':
                return None
            else:
                root = TreeNode(int(val))
                root.left = helper(data)
                root.right = helper(data)
            return root

        data = iter(data.split(","))  # make it iteratable
        return helper(data)