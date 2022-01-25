# 1688:比赛中的配对次数
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfMatches(self, n: int) -> int:
        # 总配对次数
        sums = 0
        while n > 1:
            if n % 2 == 1:
                # 奇数队伍
                # 配对次数：(n - 1) / 2
                sums += (n - 1) / 2
                # 剩余队伍数：(n - 1) / 2 + 1
                n = (n - 1) / 2 + 1
            else:
                # 偶数队伍
                # 配对次数：n / 2
                sums += n / 2
                # 剩余队伍数：n / 2
                n /= 2
        return int(sums)
# leetcode submit region end(Prohibit modification and deletion)
