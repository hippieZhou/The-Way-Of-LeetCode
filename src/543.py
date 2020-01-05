# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0
        self.get_depth(root)
        return self.res

    def get_depth(self, root) -> int:
        if not root:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        return max(left, right) + 1
