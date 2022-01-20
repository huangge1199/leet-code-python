# 567:字符串的排列
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        m, n = len(s1), len(s2)
        dic1 = [0] * 26
        dic2 = [0] * 26
        for i in range(m):
            dic1[ord(s1[i]) - ord("a")] += 1  # s1
            dic2[ord(s2[i]) - ord("a")] += 1  # s2
        if dic1 == dic2:
            return True
        for i in range(m, n):
            dic2[ord(s2[i]) - ord("a")] += 1  # 进
            dic2[ord(s2[i - m]) - ord("a")] -= 1  # 出
            if dic1 == dic2:
                return True
        return False


if __name__ == "__main__":
    Solution.checkInclusion(Solution, "ab", "eidbaooo")
# leetcode submit region end(Prohibit modification and deletion)
