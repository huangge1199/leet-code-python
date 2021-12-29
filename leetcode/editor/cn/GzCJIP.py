# 剑指 Offer II 088:爬楼梯的最少成本
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mins = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            mins[i] = min(mins[i - 2] + cost[i - 2], mins[i - 1] + cost[i - 1])
        return mins[len(cost)]
# leetcode submit region end(Prohibit modification and deletion)
