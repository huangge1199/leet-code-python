# 1725:可以形成最大正方形的矩形数目
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLength = 0
        count = 0
        for rectangle in rectangles:
            temp = min(rectangle[0], rectangle[1])
            if temp == maxLength:
                count = count + 1
            elif temp > maxLength:
                count = 1
                maxLength = temp
        return count
# leetcode submit region end(Prohibit modification and deletion)
