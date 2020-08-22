# Prefix Sum
# T:O(N) S:O(N)
class Solution:
    def pathSum(self, root, target):
        self.ans = 0
        self.cache = collections.defaultdict(int)
        self.cache[0] = 1
        self.target = target
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, cur_sum):
        if not root:
            return
        cur_sum += root.val
        self.ans += self.cache[cur_sum - self.target]

        self.cache[cur_sum] += 1
        self.dfs(root.left, cur_sum)
        self.dfs(root.right, cur_sum)
        self.cache[cur_sum] -= 1


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return

            curr_sum += node.val

            # here is the sum we're looking for
            if curr_sum == k:
                count += 1

            count += h[curr_sum - k]

            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1


            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            # remove the current sum from the hashmap
            # in order not to use it during
            # the parallel subtree processing
            h[curr_sum] -= 1

        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count