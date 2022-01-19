# 19:删除链表的倒数第 N 个结点
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size == n:
            return head.next
        size -= n
        temp = head
        while size > 1:
            temp = temp.next
            size -= 1
        temp.next = temp.next.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
