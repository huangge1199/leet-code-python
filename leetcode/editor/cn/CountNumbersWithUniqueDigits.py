# 357:统计各位数字都不同的数字个数
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        sub = 9
        count = 10
        mul = 9
        for i in range(2, n + 1):
            count += mul * sub
            mul *= sub
            sub -= 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
