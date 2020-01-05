# 翻转一棵二叉树。


class Solution:
    def invertTree(self,root):
        if root == None:
            return root
        root.left,root.right = self.invertTree(root.right,root.left)
        return root
