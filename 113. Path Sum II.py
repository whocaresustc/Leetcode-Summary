class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def pathSum(self, root, target):
        result = []
        self.dfs(root, [], result, 0,  target)
        return result

    def dfs(self, root, path, result, curSum, target):
        if not root:
            return
        curSum += root.val
        if not root.left and not root.right and curSum == target:
            result.append(path[:] + [root.val])

        self.dfs(root.left, path + [root.val], result, curSum, target)
        self.dfs(root.right, path + [root.val], result, curSum, target)
