# 2414:最长的字母序连续子字符串的长度

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt = bf = 0
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) != 1:
                cnt = max(cnt, i - bf)
                bf = i
        return max(cnt, len(s) - bf)
# leetcode submit region end(Prohibit modification and deletion)
