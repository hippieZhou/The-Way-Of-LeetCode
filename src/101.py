# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。


class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        from collections import deque
        q = deque([root, root])
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if not node1 and not node2:
                continue
            if (not node1 or not node2) or(node1.val != node2.val):
                return False
            q.extend([node1.left, node2.right, node1.right, node2.left])
        return True
