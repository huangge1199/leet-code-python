# 459:重复的子字符串
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            if len(s) % i == 0:
                if s[0:i] == s[len(s)-i:len(s)] and s[0:len(s)-i] == s[i:len(s)]:
                    return True
        return False


if __name__ == "__main__":
    Solution.repeatedSubstringPattern(Solution, "abcabcabcabc")
# leetcode submit region end(Prohibit modification and deletion)
