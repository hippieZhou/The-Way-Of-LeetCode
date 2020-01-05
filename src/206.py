# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class Solution(object):
    def reverseList(self, head):
        p = None
        while head:
            head.next, p, head = p, head, head.next
        return p
