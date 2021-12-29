# 1991:找到数组的中间位置
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        if size == 2:
            if nums[1] == 0:
                return 0
            elif nums[0] == 0:
                return 1
            else:
                return -1
        re_nums = [0] * size
        re_nums[size - 1] = nums[size - 1]
        for i in range(1, size):
            re_nums[size - 1 - i] = re_nums[size - i] + nums[size - 1 - i]
        for j in range(0, size):
            if j == 0:
                if re_nums[j + 1] == 0:
                    return 0
            elif j == size - 1:
                if nums[j - 1] == 0:
                    return size - 1
            else:
                if nums[j - 1] == re_nums[j + 1]:
                    return j
                else:
                    nums[j] += nums[j - 1]
        return -1
        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    Solution.findMiddleIndex(Solution, [2, 3, -1, 8, 4])
