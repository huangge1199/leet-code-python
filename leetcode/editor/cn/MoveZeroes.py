# 283:移动零
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if index < i:
                    nums[index] = nums[i]
                index += 1
        nums[:] = nums[:index] + [0] * (len(nums) - index)
# leetcode submit region end(Prohibit modification and deletion)
