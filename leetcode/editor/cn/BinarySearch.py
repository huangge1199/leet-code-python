# 704:二分查找
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end >= start:
            mid = int((start + end) / 2)
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    Solution.search(Solution, [5], 5)
# leetcode submit region end(Prohibit modification and deletion)
