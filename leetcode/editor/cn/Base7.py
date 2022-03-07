# 504:七进制数
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToBase7(self, num: int) -> str:
        bl = num < 0
        s = ''
        num = abs(num)
        while num >= 7:
            s = str(num % 7) + s
            num //= 7
        s = str(num) + s
        if bl:
            s = '-' + s
        return s


if __name__ == '__main__':
    Solution.convertToBase7(Solution, 100)
# leetcode submit region end(Prohibit modification and deletion)
