class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-",  "*", "/"]
        stack = []
        for t in tokens:
            if t in ops:
                if t == "+":
                    stack.append(stack.pop(-2) + stack.pop(-1))
                elif t == "-":
                    stack.append(stack.pop(-2) - stack.pop(-1))
                elif t == "*":
                    stack.append(stack.pop(-2) * stack.pop(-1))
                elif t == "/":
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                else:
                    return -1
            else:
                stack.append(int(t))
        return int(stack[-1])