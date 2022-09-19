# 2415:反转二叉树的奇数层
from typing import Optional

from leetcode.editor.cn.entity import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = 1
        while queue[0].left:
            next = []
            for node in queue:
                next += [node.left, node.right]
            queue = next
            if level:
                for i in range(len(queue) // 2):
                    node1, node2 = queue[i], queue[len(queue) - 1 - i]
                    node1.val, node2.val = node2.val, node1.val
            level = 1 - level
        return root
# leetcode submit region end(Prohibit modification and deletion)
