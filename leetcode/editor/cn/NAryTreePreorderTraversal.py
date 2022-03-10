# 589:N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                for child in node.children:
                    dfs(child)

        dfs(root)
        return result
# leetcode submit region end(Prohibit modification and deletion)
