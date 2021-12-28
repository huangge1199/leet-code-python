# 找出数组中重复的数字。 
# 
#  
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。 
# 
#  示例 1： 
# 
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
#  
# 
#  
# 
#  限制： 
# 
#  2 <= n <= 100000 
#  Related Topics 数组 哈希表 排序 👍 650 👎 0


# 剑指 Offer 03:数组中重复的数字剑指 Offer 03:数组中重复的数字
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # sorted(nums)
        nums.sort()
        for i in range(len(nums)):
            if (i > 0) & (nums[i] == nums[i - 1]):
                return nums[i]


if __name__ == "__main__":
    print(Solution().findRepeatNumber([1, 1, 1]))
    print(Solution().findRepeatNumber([3, 1, 2, 3]))
# leetcode submit region end(Prohibit modification and deletion)
