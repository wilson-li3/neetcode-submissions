class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []
        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                if t == "+":
                    temp = int(stack.pop()) + int(stack.pop())
                    stack.append(temp)
                elif t == "*":
                    temp = int(stack.pop()) * int(stack.pop())
                    stack.append(temp)
                elif t == "/":
                    temp1 = int(stack.pop()) 
                    temp2 = int(stack.pop())
                    stack.append(int(temp2 / temp1))
                elif t == "-":
                    temp1 = int(stack.pop()) 
                    temp2 = int(stack.pop())
                    stack.append(temp2 - temp1)
        return int(stack[-1])

