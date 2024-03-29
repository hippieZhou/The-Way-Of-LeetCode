# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
       def maxDepth(self, root: TreeNode) -> int:
           return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
           
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
