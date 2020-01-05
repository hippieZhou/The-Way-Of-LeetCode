# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。


class Solution:
    def sortedArrayToBST(self, nums: list) -> list:
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[mid+1:])
            return node


v = Solution().sortedArrayToBST([-10, -3, 0, 5])
print(v)
