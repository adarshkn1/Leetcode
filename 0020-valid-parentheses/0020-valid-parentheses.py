class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        for sym in s:
            if(sym == '(' or sym == '[' or sym == '{'):
                stack.append(sym)
                top = top+1
            
            if(len(stack)==0):
                return False
            
            if((sym ==')'and (stack[top] == '[' or stack[top] == '{')) or (sym == ']' and (stack[top] == '(' or stack[top] == '{'))  or (sym =='}'and (stack[top] == '[' or stack[top] == '('))):
                return False
            
            if((sym ==')'and stack[top] == '(') or (sym == ']' and stack[top] == '[')  or (sym =='}'and stack[top] == '{')):
                stack.pop()
                top = top-1

        if(top == -1):
            return True
        else:
            return False

        