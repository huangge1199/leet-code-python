# 35:搜索插入位置
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            # if nums[i] == target | nums[i] > target:
            if nums[i] == target or nums[i] > target:
                return i
        return len(nums)

# leetcode submit region end(Prohibit modification and deletion)
