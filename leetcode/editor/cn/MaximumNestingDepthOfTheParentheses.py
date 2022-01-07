# 1614:括号的最大嵌套深度
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        result = 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                result = max(result, count)
            elif s[i] == ')':
                count -= 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
