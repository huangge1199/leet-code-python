# 1219:黄金矿工
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            count = grid[x][y]
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0 or use[nx][ny]:
                    continue
                use[nx][ny] = True
                count = max(count, grid[x][y] + dfs(nx, ny))
                use[nx][ny] = False
            return count

        counts = 0
        # 这种形式下，给一个元素赋值，对应的所有行相同列都会赋值
        # use = [[False] * len(grid[0])] * len(grid)
        use = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    use[i][j] = True
                    counts = max(counts, dfs(i, j))
                    use[i][j] = False
        return counts


if __name__ == "__main__":
    Solution.getMaximumGold(Solution, [[0, 6, 0], [5, 8, 7], [0, 9, 0]])
# leetcode submit region end(Prohibit modification and deletion)
