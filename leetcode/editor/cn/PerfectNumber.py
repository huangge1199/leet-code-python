# 507:完美数
# leetcode submit region begin(Prohibit modification and deletion)
from math import sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                sum += i + num / i
        return num == sum + 1 and num != 1


if __name__ == "__main__":
    Solution.checkPerfectNumber(Solution, 28)
# leetcode submit region end(Prohibit modification and deletion)
