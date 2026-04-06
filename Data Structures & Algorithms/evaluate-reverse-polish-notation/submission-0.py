class Solution:
    def eval(self, num1, num2, op):
        num1, num2 = int(num1), int(num2)
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
        else:
            return None
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for el in tokens:
            if el in ops:
                r = self.eval(stack[-2], stack[-1], el)
                stack.pop()
                stack.pop()
                stack.append(r)
                continue
            stack.append(el)
        return int(stack[-1])