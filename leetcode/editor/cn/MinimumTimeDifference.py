# 539:最小时间差
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [0] * 2880
        for timePoint in timePoints:
            time = int(timePoint[:2]) * 60 + int(timePoint[-2:])
            if times[time] == 1:
                return 0
            times[time] = 1
            times[time + 1440] = 1
        result = 1440
        bef = 0
        for i in range(2880):
            if times[i] == 1:
                if bef > 0:
                    result = min(result, i - bef)
                if i > 1439:
                    break
                bef = i
        return result
# leetcode submit region end(Prohibit modification and deletion)
