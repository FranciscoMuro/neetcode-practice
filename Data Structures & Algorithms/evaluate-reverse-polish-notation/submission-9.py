class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        # First edge case could be if we only have a number in the list of tokens like 
        #["1"]
        # to check that we can use
        if len(tokens) == 1 and tokens[0] not in operators and type(tokens[0]) == str:
            return int(tokens[0])
        # here we go in each token if the token is not an operator is a number so we push it into the stack.
        for token in tokens:

            # so the token is a number?
            if token not in operators:
                stack.append(token)
            # now we check witch operator we have and perform a operation
            # and also check if the stack has values in it
            if len(stack) != 0 and token == '*':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val1*val2)
            if len(stack) != 0 and token == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val2/val1)
            if len(stack) != 0 and token == '+':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val1+val2)
            if len(stack) != 0 and token == '-':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                stack.append(val2-val1)

        return int(stack.pop())
            
                
            