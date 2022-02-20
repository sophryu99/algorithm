# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.stck = []
        
    def push(self, x: int) -> None:
        self.stck.append(x)

    def pop(self) -> int:
        return self.stck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def empty(self) -> bool:
        if not self.stck:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()