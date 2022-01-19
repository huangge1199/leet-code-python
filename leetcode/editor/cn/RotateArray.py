# 189:轮转数组
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
# leetcode submit region end(Prohibit modification and deletion)
