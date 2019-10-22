# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list:
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root: TreeNode, ans: list):
        if root:
            if root.left:
                self.helper(root.left, ans)
            ans.append(root.val)
            if root.right:
                self.helper(root.right, ans)
