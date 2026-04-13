class Solution:
    def isValid(self, s: str) -> bool:
        # creating a stack 
        stack = []
        # creating a dictionary with close to open paranthesis as key value pair 
        closetoopen = {']':'[',')':'(','}':'{'}
        #iterate through the string s 
        for c in s:
            # if c is in closeToOpen that means c is a closing bracket, then check if there is a corresponsing opening bracket
            if c in closetoopen:
                if stack and stack[-1]==closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        