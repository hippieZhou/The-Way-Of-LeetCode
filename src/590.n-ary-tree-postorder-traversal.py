class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# class Solution:
#     def postorder(self, root: Node) -> list:
#         ans = []
#         self.recursion(root, ans)
#         return ans

#     def recursion(self, root: Node, ans: list):
#         if not root:
#             return

#         for child in root.children:
#             self.recursion(child)

#         ans.append(root.val)


class Solution:
    def postorder(self, root: Node) -> list:
        ans = []

        def recursion(root: Node, array: list):
            for child in root.children:
                recursion(child, array)
            array.append(root.val)

        if root:
            recursion(root, ans)

        return ans
