class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root:
                return None

            root_deleted = root.val in to_delete_set
            # if root and not to be deleted
            if is_root and not root_deleted:
                res.append(root)
            # if root_deleted is True, then root.left become root, so is_root = root_deleted = True
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)

            return None if root_deleted else root

        helper(root, True)
        return res