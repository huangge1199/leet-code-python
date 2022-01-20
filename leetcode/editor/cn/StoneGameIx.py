# 2029:石子游戏 IX
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0] * 3
        for stone in stones:
            counts[stone % 3] += 1
        if counts[0] % 2 == 0:
            return counts[1] > 0 and counts[2] > 0
        else:
            return abs(counts[1] - counts[2]) > 2
# leetcode submit region end(Prohibit modification and deletion)
