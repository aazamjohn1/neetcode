
class MinStack:

    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Min stack to store minimum value at each level
        self.min_stack = []
        

    def push(self, val: int) -> None:
        # Add value to main stack
        self.stack.append(val)
        
        # Determine the new minimum
        # If min_stack is empty, val is the minimum
        # Otherwise, compare val with current minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Store the smaller of val and current minimum
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)
        

    def pop(self) -> None:
        # Remove from both stacks to keep them synchronized
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        # Return the last element without removing it
        return self.stack[-1]
        

    def getMin(self) -> int:
        # The top of min_stack always has the current minimum
        return self.min_stack[-1]
