# 剑指 Offer 06:从尾到头打印链表
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        return num[::-1]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# leetcode submit region end(Prohibit modification and deletion)
