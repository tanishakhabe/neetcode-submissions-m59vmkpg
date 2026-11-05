class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store (temp, index)
        res = [0] * len(temperatures)

        for i, x in enumerate(temperatures):
            while stack and stack[-1][0] < x:
                j_temp, j_index = stack.pop()
                res[j_index] = i - j_index
            stack.append((x, i)) 
        return res
        