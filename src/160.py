# 编写一个程序，找到两个单链表相交的起始节点。


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = (headA, headB) if headA and headB else (None, None)
        while a != b:
            a, b = not a and headB or a.next, not b and headA or b.next
        return a
