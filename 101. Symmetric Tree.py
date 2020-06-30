class Solution:

    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False


def isSymmetric(self, root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True