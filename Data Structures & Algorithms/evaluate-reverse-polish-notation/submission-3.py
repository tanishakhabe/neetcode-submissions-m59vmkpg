class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens: 
            if token not in {"+", "-", "*", "/"}:
                num = int(token)
                stack.append(num)
            else:
                first = stack.pop() #top
                second = stack.pop() #bottom
                

                if token == "+":
                    stack.append(first + second)
                if token == "-":
                    stack.append(second - first)

                if token == "*":
                    stack.append(first * second)

                if token == "/":
                    stack.append(int(second / first))
        return stack[0]



        
        