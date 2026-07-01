class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        
        for t in tokens:
            print(stack, t)
            if t in ['+', '-', '*', '/']:
                op1 = stack.pop()
                op2 = stack.pop()
                print(op1, op2)
                if t == "+":
                    stack.append(op1+op2)
                elif t == "*":
                    stack.append(op1*op2)
                elif t == "-":
                    stack.append(op2-op1)
                elif t == "/":
                    stack.append(int(op2/op1))
            else:
                stack.append(int(t))
        
        return stack[0]
        