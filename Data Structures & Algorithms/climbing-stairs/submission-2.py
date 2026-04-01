class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: 
            return n
        
        else: 
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# simplest case: 1 stair
# only 1 way (take 1 step)

# 2 stairs
# 1 + 1 
# 2

# 3 stairs
# 1 + 1 + 1
# 2 + 1
# 1 + 2

# 4 stairs
# 1 + 1 + 1 + 1 
# 1 + 1 + 2
# 2 + 1 + 1 
# 1 + 2 + 1
# 2 + 2


# 5 stairs 
# 


