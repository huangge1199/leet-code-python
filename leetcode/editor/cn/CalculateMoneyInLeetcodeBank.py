# 1716:计算力扣银行的钱
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalMoney(self, n: int) -> int:
        count = int(n / 7)
        bef = int((56 + 7 * (count - 1)) * count / 2)
        index = int(n % 7)
        aft = int((2 * count + index + 1) * index / 2)
        return bef + aft


if __name__ == "__main__":
    Solution.totalMoney(Solution, 10)
# leetcode submit region end(Prohibit modification and deletion)
