# 798:得分最高的最小轮调
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        size = len(nums)
        arrs = [0] * (size + 1)
        for i in range(size):
            left = (i + 1) % size
            right = (i - nums[i] + size) % size
            if left > right:
                arrs[0] += 1
                arrs[size] -= 1
            arrs[left] += 1
            arrs[right + 1] -= 1
        for i in range(1, size + 1):
            arrs[i] += arrs[i - 1]
        result = 0
        for i in range(1, size + 1):
            if arrs[i] > arrs[result]:
                result = i
        return result
# leetcode submit region end(Prohibit modification and deletion)
