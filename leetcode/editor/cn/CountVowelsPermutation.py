# 1220:统计元音字母序列的数目
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9) + 7
        nums = [[1] * 5] + [[0] * 5 for i in range(n - 1)]
        for i in range(1, n):
            nums[i][0] = (nums[i - 1][1] + nums[i - 1][2] + nums[i - 1][4]) % mod
            nums[i][1] = (nums[i - 1][0] + nums[i - 1][2]) % mod
            nums[i][2] = (nums[i - 1][1] + nums[i - 1][3]) % mod
            nums[i][3] = nums[i - 1][2]
            nums[i][4] = (nums[i - 1][2] + nums[i - 1][3]) % mod
        result = 0
        for i in range(5):
            result += nums[-1][i]
        return int(result % mod)


if __name__ == "__main__":
    Solution.countVowelPermutation(Solution, 5)
# leetcode submit region end(Prohibit modification and deletion)
