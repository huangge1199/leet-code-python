# 540:有序数组中的单一元素
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num = nums[0]
        for i in range(1, len(nums)):
            num = num ^ nums[i]
        return num
# leetcode submit region end(Prohibit modification and deletion)
