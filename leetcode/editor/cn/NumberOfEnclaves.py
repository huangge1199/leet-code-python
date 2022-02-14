# 1020:飞地的数量
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List, Type


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        use = [[False] * len(grid[0]) for _ in range(len(grid))]
        queue = deque()
        xl = len(grid)
        yl = len(grid[0])
        count = 0
        for i in range(xl):
            if grid[i][0] == 1:
                queue.append((i, 0))
                use[i][0] = True
                count += 1
            if grid[i][yl - 1] == 1 and not use[i][yl - 1]:
                queue.append((i, yl - 1))
                use[i][yl - 1] = True
                count += 1
        for i in range(1, yl - 1):
            if grid[0][i] == 1 and not use[0][i]:
                queue.append((0, i))
                use[0][i] = True
                count += 1
            if grid[xl - 1][i] == 1 and not use[xl - 1][i]:
                queue.append((xl - 1, i))
                use[xl - 1][i] = True
                count += 1
        while queue:
            x, y = queue.pop()
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0 or use[nx][ny]:
                    continue
                queue.append((nx, ny))
                use[nx][ny] = True
                count += 1
        sc = sum([sum(row) for row in grid])
        return sc - count


if __name__ == "__main__":
    Solution.numEnclaves(Type[Solution], [[0], [1], [1], [0], [0]])
# leetcode submit region end(Prohibit modification and deletion)
