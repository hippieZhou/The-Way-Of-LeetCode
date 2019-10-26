# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(root: TreeNode):
            return recursion(root.left) + [root.val] + recursion(root.right) if root else []

        self.ans = recursion(root)
        return self.ans == list(sorted(set(self.ans)))

    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None

        def helper(root: TreeNode):
            if not root:
                return True
            if not helper(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root
            return helper(root.right)

        return helper(root)
