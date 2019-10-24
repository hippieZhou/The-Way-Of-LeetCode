class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list:
        q, ans = [root], []
        while any(q):
            ans.append([item.val for item in q])
            q = [child for item in q for child in item.children if child]
        return ans
