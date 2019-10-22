# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root: TreeNode, ans: list):
        if root:
            ans.append(root.val)
            if root.left:
                self.helper(root.left, ans)
            if root.right:
                self.helper(root.right, ans)
