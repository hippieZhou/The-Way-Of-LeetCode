# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归的实现方法
    def levelOrder(self, root: TreeNode) -> list:
        levels = []
        if not root:
            return levels

        def helper(node: TreeNode, level: int):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level+1)
        helper(root, 0)
        return levels
