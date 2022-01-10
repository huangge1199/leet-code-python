# 306:累加数
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def helper(a, b):
            i, j, res, one = len(a) - 1, len(b) - 1, [], 0
            while i >= 0 or j >= 0:
                curA = curB = 0
                if i >= 0:
                    curA = int(a[i])
                    i -= 1
                if j >= 0:
                    curB = int(b[j])
                    j -= 1
                cur = curA + curB + one
                if cur >= 10:
                    cur %= 10
                    one = 1
                else:
                    one = 0
                res.append(str(cur))
            if one:
                res.append("1")
            return "".join(res[::-1])

        def dfs(p, q):
            last, first, second = 0, p, q
            while second < len(num):
                if (num[last] == '0' and first > last + 1) or (num[first] == '0' and second > first + 1):
                    return False
                s = helper(num[last:first], num[first:second])
                if num[second:second + len(s)] != s:
                    return False
                last, first, second = first, second, second + len(s)
            return True

        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                if dfs(i, j):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
