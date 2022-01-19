# 557:反转字符串中的单词 III
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]
# leetcode submit region end(Prohibit modification and deletion)
