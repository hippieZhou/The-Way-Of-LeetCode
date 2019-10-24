"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def recursion(root:'Node', array:list):
            array.append(root.val)
            for child in root.children:
                recursion(child, array)
                
        if root:
            recursion(root, ans)
        
        return ans