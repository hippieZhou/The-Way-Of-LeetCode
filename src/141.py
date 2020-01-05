# 给定一个链表，判断链表中是否有环。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。


class Solution(object):
    def hasCycle(self, head):
        haxi = set()
        while head:
            if head in haxi:
                return True
            haxi.ad
            head = head.next
        return False

        # while head:
        #     if array.count(head.val) > 0:
        #         return True
        #     else:
        #         array.append(head.val)
        #     head = head.next
        # return False
