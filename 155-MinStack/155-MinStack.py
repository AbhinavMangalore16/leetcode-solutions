# Last updated: 3/31/2026, 9:39:22 PM
class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        minn = min(val,self.minstk[-1] if self.minstk else val)
        self.minstk.append(minn)

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()