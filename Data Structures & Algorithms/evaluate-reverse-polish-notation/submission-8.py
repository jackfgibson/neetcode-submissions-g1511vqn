class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                operate = int(stack[-2])+int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(operate)
            elif token == "-":
                operate = int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(operate)
            elif token == "*":
                operate = int(stack[-2])*int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(operate)
            elif token == "/":
                operate = int(int(stack[-2])/(int(stack[-1])))
                stack.pop()
                stack.pop()
                stack.append(operate)
            else:
                stack.append(token)
        return int(stack[0])