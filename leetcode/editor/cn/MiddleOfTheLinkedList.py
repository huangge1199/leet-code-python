# 876:链表的中间结点
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size += 1
        size = int(size / 2)
        temp = head
        while size > 0:
            temp = temp.next
            size -= 1
        return temp
# leetcode submit region end(Prohibit modification and deletion)
