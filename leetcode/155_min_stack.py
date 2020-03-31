class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        if not self.data:
            current_min = x
        else:
            current_min = self.getMin()
        if x < current_min:
            self.data.append((x, x))
        else:
            self.data.append((x, current_min))

    def pop(self) -> None:
        del self.data[len(self.data)-1]

    def top(self) -> int:
        return self.data[len(self.data)-1][0]

    def getMin(self) -> int:
        return self.data[len(self.data)-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.data)
print(obj.getMin())
obj.pop()
print(obj.data)
print(obj.top())
print(obj.getMin())