class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
    ')': '(',
    ']': '[',
    '}': '{'}
        stack=[]
        for bracket in s:
            if bracket in pairs:
                if not stack:
                    return False
                if pairs[bracket]!=stack[-1]:
                    return False
                stack.pop() 
            else:  
                stack.append(bracket)
        return len(stack)==0

        