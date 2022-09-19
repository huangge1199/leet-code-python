# 2413:最小偶倍数
from math import lcm


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(n, 2)
# leetcode submit region end(Prohibit modification and deletion)
