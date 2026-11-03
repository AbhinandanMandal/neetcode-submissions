
from collections import deque
class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
        

    def push(self, x: int) -> None:
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.popleft())
        self.que1, self.que2 = self.que2, self.que1
        

    def pop(self) -> int:
        if not self.empty():
            return self.que1.popleft()
            
    def top(self) -> int:
        if not self.empty():
            return self.que1[0]
        

    def empty(self) -> bool:
        return len(self.que1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()