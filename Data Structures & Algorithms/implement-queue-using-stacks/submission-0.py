from collections import deque

class MyQueue:
    def __init__(self):
        self.stack1 = deque()  # Input stack
        self.stack2 = deque()  # Output stack

    def push(self, n):
        # Push all elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        # Push the new element into stack1
        self.stack1.append(n)
        
        # Push everything back from stack2 to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        if not self.empty():
            return self.stack1.pop()

    def peek(self):
        if not self.empty():
            return self.stack1[-1]

    def empty(self):
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()