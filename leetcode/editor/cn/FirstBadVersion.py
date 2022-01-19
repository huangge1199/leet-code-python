# 278:第一个错误的版本
# leetcode submit region begin(Prohibit modification and deletion)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(mid):
    return mid > 3


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = int((end - start) / 2 + start)
            if (isBadVersion(mid)):
                end = mid
            else:
                start = mid + 1
        if (isBadVersion(start)):
            return int(start)
        else:
            return int(end)


if __name__ == "__main__":
    Solution.firstBadVersion(Solution, 5)
# leetcode submit region end(Prohibit modification and deletion)
