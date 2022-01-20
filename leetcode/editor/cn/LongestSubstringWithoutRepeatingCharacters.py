# 3:无重复字符的最长子串
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        result = 0
        chs = set()
        for i in range(len(s)):
            if i > 0:
                chs.remove(s[i - 1])
            while right < len(s) and s[right] not in chs:
                chs.add(s[right])
                right += 1
            result = max(result, right - i)
        return result


if __name__ == "__main__":
    Solution.lengthOfLongestSubstring(Solution, "abcabcbb")

# leetcode submit region end(Prohibit modification and deletion)
