class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):  # return the maximum including the node
            nonlocal
            max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            cur_max = node.val + left_gain + right_gain

            # update max_sum
            max_sum = max(max_sum, cur_max)

            # either left or right because it includes the node itself
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum