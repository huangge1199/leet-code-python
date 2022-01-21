# 1345:跳跃游戏 IV
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        map = defaultdict(list)
        for i, a in enumerate(arr):
            map[a].append(i)
        use = set()
        queue = deque()
        queue.append(0)
        use.add(0)
        count = 0
        while queue:
            count += 1
            for i in range(len(queue)):
                index = queue.popleft()
                if index - 1 >= 0 and (index - 1) not in use:
                    use.add(index - 1)
                    queue.append(index - 1)
                if index + 1 == len(arr) - 1:
                    return count
                if index + 1 < len(arr) and (index + 1) not in use:
                    use.add(index + 1)
                    queue.append(index + 1)
                v = arr[index]
                for i in map[v]:
                    if i == len(arr) - 1:
                        return count
                    if i not in use:
                        use.add(i)
                        queue.append(i)
                del map[v]


if __name__ == "__main__":
    Solution.minJumps(Solution, "[100,-23,-23,404,100,23,23,23,3,404]")
# leetcode submit region end(Prohibit modification and deletion)
