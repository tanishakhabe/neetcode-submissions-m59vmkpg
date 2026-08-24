class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for paren in s:
            if paren in paren_map.values():
                stack.append(paren)
            else:
                if stack and paren_map[paren] == stack[-1]:
                    stack.pop()
                else:
                    return False 
                    
        if len(stack) != 0: return False
        return True

