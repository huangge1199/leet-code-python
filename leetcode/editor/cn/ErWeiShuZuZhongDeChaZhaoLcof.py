# 剑指 Offer 04:二维数组中的查找
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


if __name__ == "__main__":
    Solution.findNumberIn2DArray(Solution,
                                 [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                                  [18, 21, 23, 26, 30]], 5)
# leetcode submit region end(Prohibit modification and deletion)
