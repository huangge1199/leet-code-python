# 344:反转字符串
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(int(n / 2)):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
# leetcode submit region end(Prohibit modification and deletion)
