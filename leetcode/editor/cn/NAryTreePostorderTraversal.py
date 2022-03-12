# 590:N 叉树的后序遍历
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []

        def dfs(root1: 'Node'):
            if root1 is None:
                return
            if len(root1.children)==0:
                arr.append(root1.val)
                return
            for node in root1.children:
                dfs(node)
            arr.append(root1.val)
        dfs(root)
        return arr
# leetcode submit region end(Prohibit modification and deletion)
