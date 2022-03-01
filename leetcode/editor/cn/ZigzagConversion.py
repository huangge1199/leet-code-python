# 6:Z 字形变换
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        mat = [[''] * len(s) for _ in range(numRows)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % (numRows * 2 - 2) < numRows - 1:
                x += 1
            else:
                x -= 1
                y += 1
        return ''.join(ch for row in mat for ch in row if ch)
