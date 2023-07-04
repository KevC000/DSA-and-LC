#Min Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
            
    def pop(self) -> None: 
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
    
# Time O(N), Space O(N)
# Use 1 stack to keep track of the values and another to keep track of the running minimum.