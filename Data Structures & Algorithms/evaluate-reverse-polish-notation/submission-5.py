class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        if (len(tokens) == 1 and tokens[0] not in operators and type(tokens[0]) == str):
            return int(tokens[0])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            if (token == "*" and len(stack) != 0):
                temVal1 = int(stack.pop())
                temVal2 = int(stack.pop())
                stack.append(temVal1*temVal2)
            if (token == "/" and len(stack) != 0):
                temVal1 = int(stack.pop())
                temVal2 = int(stack.pop())
                stack.append(float(temVal2)/temVal1)
            if (token == "+" and len(stack) != 0):
                temVal1 = int(stack.pop())
                temVal2 = int(stack.pop())
                stack.append(temVal1+temVal2)
            if (token == "-" and len(stack) != 0):
                temVal1 = int(stack.pop())
                temVal2 = int(stack.pop())
                stack.append(temVal2-temVal1)
        return int(stack.pop())