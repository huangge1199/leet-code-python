# 剑指 Offer 09:用两个栈实现队列
# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:

    def __init__(self):
        self.start = []
        self.end = []

    def appendTail(self, value: int) -> None:
        self.start.append(value)

    def deleteHead(self) -> int:
        if self.end:
            return self.end.pop()
        elif not self.start:
            return -1
        else:
            while self.start:
                self.end.append(self.start.pop())
            return self.end.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
# leetcode submit region end(Prohibit modification and deletion)
