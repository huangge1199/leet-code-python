# 剑指 Offer 07:重建二叉树
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        n = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:n + 1], inorder[0:n])
        root.right = self.buildTree(preorder[n + 1:len(preorder)], inorder[n + 1:len(preorder)])
        return root


if __name__ == "__main__":
    Solution.buildTree(Solution, [3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
# leetcode submit region end(Prohibit modification and deletion)
