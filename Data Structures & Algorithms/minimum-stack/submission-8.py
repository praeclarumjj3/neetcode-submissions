class MinStack:

    def __init__(self):
        self.stack = []
        self.mi = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mi is None or val < self.mi:
            self.mi = val

    def pop(self) -> None:
        el = self.stack.pop()
        if el == self.mi and len(self.stack) > 0:
            self.mi = min(self.stack)
        elif len(self.stack) == 0:
            self.mi = None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mi