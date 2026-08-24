class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # store pairs [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_index, prev_temp = stack.pop()
                res[prev_index] = i - prev_index
            
            stack.append([i, t])
        
        return res
