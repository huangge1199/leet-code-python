# 747:至少是其他数字两倍的最大数
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >= nums[1]:
            index = 0
            max = nums[0]
            sed = nums[1]
        else:
            index = 1
            max = nums[1]
            sed = nums[0]
        for i in range(2, len(nums)):
            if nums[i] > max:
                sed = max
                max = nums[i]
                index = i
            elif nums[i] > sed:
                sed = nums[i]
        if max >= sed * 2:
            return index
        else:
            return -1


if __name__ == "__main__":
    Solution.dominantIndex(Solution, [1, 2, 3, 4])
# leetcode submit region end(Prohibit modification and deletion)
