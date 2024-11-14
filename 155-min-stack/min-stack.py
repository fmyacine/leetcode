class MinStack:
    
    def __init__(self):
        self.stack = {}
        self.cpt = 0

    def push(self, val: int) -> None:
        self.stack[self.cpt] = val
        self.cpt += 1

    def pop(self) -> None:
        self.stack.popitem()
        self.cpt -= 1
        
    def top(self) -> int:
        return list(self.stack.values())[-1]

    def getMin(self) -> int:
        return min(self.stack.values())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()