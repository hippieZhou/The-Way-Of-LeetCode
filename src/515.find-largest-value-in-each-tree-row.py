# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> list:
        ans = []

        def dfs(node: TreeNode, level: int):
            if not node:
                return

            if(len(ans)) < level:
                ans.append(node.val)
            else:
                ans[level] = max(node.val, ans[level])

            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        return ans

    def largestValues(self, root: TreeNode) -> list:
        ans = []
        row = [root]
        while any(row):
            ans.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return ans
