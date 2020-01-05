# 给定一个二叉树，它的每个结点都存放着一个整数值。

# 找出路径和等于给定数值的路径总数。

# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。


class Solution:
    def pathSum(self, root, sum: int) -> int:
        def pathFromRoot(root, sum: int) -> int:
            if not root:
                return 0
            res1 = pathFromRoot(root.left, sum-root.val)
            res2 = pathFromRoot(root.right, sum-root.val)
            res = res1 + res2
            if root.val == sum:
                res = res1 + res2 + 1
            return res
        if not root:
            return 0
        count1 = pathFromRoot(root, sum)
        count2 = self.pathSum(root.left, sum)
        count3 = self.pathSum(root.right, sum)
        return count1 + count2 + count3
