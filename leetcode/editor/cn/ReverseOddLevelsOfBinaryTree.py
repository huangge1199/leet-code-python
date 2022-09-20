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
        # BFS
        # queue = [root]
        # level = 1
        # while queue[0].left:
        #     next = []
        #     for node in queue:
        #         next += [node.left, node.right]
        #     queue = next
        #     if level:
        #         for i in range(len(queue) // 2):
        #             node1, node2 = queue[i], queue[len(queue) - 1 - i]
        #             node1.val, node2.val = node2.val, node1.val
        #     level = 1 - level
        # return root
        def dfs(left, right, level: bool) -> None:
            if left is None: return
            if level: left.val, right.val = right.val, left.val
            dfs(left.left, right.right, not level)
            dfs(left.right, right.left, not level)

        dfs(root.left,root.right, True)
        return root
# leetcode submit region end(Prohibit modification and deletion)
