# 1984:学生分数的最小差值
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k > 1:
            num = sorted(nums)
            return min(num[i + k - 1] - num[i] for i in range(len(num) - k + 1))
        else:
            return 0
# leetcode submit region end(Prohibit modification and deletion)
