# 请判断一个链表是否为回文链表。


class Solution(object):
    def isPalindrome(self, head) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
