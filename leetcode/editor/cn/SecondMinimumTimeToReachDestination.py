# 2045:到达目的地的第二短时间
# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque, defaultdict
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 统计所有节点的联通节点，并将其存入map中留着后面使用
        maps = defaultdict(list)
        for edge in edges:
            maps[edge[0]].append(edge[1])
            maps[edge[1]].append(edge[0])
        queue = deque([1])
        # 记录节点到达的次数
        counts = defaultdict(int)
        # 记录到达节点的时间
        free = 0
        while queue:
            # 红灯情况下加上需要等待的时间
            if free % (2 * change) >= change:
                free += change - free % change
            free += time
            # 同一时间可以到达的节点数量
            size = len(queue)
            # 同一时间节点是否已经到达
            use = defaultdict(bool)
            for i in range(size):
                for num in maps[queue.popleft()]:
                    # 同一时间未到达，并且到达该节点的总次数小于2
                    if not use[num] and counts[num] < 2:
                        queue.append(num)
                        use[num] = True
                        counts[num] += 1

                    # 如果是第二次到达最后一个节点，直接返回需要到达的诗句
                    if num == n and counts[num] == 2:
                        return free
        return 0


if __name__ == "__main__":
    Solution.secondMinimum(Solution, 5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 3)
# leetcode submit region end(Prohibit modification and deletion)
