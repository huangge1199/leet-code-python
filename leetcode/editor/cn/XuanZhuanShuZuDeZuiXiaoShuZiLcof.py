# 剑指 Offer 11:旋转数组的最小数字
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        start = 0
        end = len(numbers) - 1
        while start < end:
            mid = start + (end - start) // 2
            if numbers[mid] < numbers[end]:
                end = mid
            elif numbers[mid] > numbers[end]:
                start = mid + 1
            else:
                end -= 1
        return numbers[start]
# leetcode submit region end(Prohibit modification and deletion)
