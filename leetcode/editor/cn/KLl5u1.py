# 剑指 Offer II 006:排序数组中两个数字之和
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sum_num = numbers[start] + numbers[end]
            if sum_num == target:
                break
            elif sum_num < target:
                start += 1
            else:
                end -= 1
        return [start, end]
# leetcode submit region end(Prohibit modification and deletion)
