class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None

        # tree s and t are exactly the same
        if s.val == t.val and self.compare(s, t):
            return True

        # subtree of the left or right
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def compare(self, s, t):
        if s is None:
            return t is None

        if t is None or s.val != t.val:
            return False

        return self.compare(s.left, t.left) and self.compare(s.right, t.right)
