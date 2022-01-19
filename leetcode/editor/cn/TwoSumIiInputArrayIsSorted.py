# 167:两数之和 II - 输入有序数组
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if target == numbers[start] + numbers[end]:
                break
            elif target > numbers[start] + numbers[end]:
                start += 1
            else:
                end -= 1
        return [start + 1, end + 1]
# leetcode submit region end(Prohibit modification and deletion)
