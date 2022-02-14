# 1189:“气球” 的最大数量
# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(cnts[ch] // 2 if ch in "lo" else cnts[ch] for ch in "balon") if (cnts := Counter(text)) else 0


if __name__ == "__main__":
    print(Solution.maxNumberOfBalloons(Solution, "balon"))
# leetcode submit region end(Prohibit modification and deletion)
