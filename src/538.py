# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。


class Solution:
    def convertBST(self, root):
        if not root:
            return root
        stack = []
        cur = root
        sum = 0
        while cur or stack:
            stack.append(cur)
            cur = cur.right
        cur = stack.pop(-1)
        sum += cur.val
        cur.val = sum
        cur = cur.left
    return root
