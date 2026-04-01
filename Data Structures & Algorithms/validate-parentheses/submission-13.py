class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { "(" : ")", "[" : "]", "{" : "}" }
        for c in s:
            if c in closeToOpen:
                stack.append(c)
            else:
                if stack and closeToOpen.get(stack[-1]) == c:
                    stack.pop()
                else:
                    return False


        if len(stack) != 0:
            return False
        else:
            return True