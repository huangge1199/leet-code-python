# 977:有序数组的平方
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)
# leetcode submit region end(Prohibit modification and deletion)
