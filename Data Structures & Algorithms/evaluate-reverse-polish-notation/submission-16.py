class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        stack = []
        
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                self.doOperation(t, stack)
            print(stack)
        
        return int(stack.pop())

    def doOperation(self, operator, stack):
            if operator == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) + int(val2))
            elif operator == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) - int(val1))
            elif operator == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) * int(val2))
            elif operator == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) / int(val1))