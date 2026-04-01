class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        
        for elem in s:
            if elem in map.values():
                stack.append(elem)
            else: 
                if stack and map[elem] == stack[-1]:
                    stack.pop()
                else: return False
        return len(stack) == 0


    

            






# time complexity: 
# space complexity: 