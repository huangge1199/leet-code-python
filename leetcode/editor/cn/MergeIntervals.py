# 56:合并区间
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nums = []
        intervals.sort(key=lambda x: x[0])
        nums.append(intervals[0])
        index = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] > nums[index][1]:
                nums.append(intervals[i])
                index += 1
            else:
                nums[index][1] = max(nums[index][1], intervals[i][1])
        return nums
# leetcode submit region end(Prohibit modification and deletion)
