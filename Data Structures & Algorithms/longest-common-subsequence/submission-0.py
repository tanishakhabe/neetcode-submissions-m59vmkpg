class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        

        def dp(i, j):
            if i == 0 or j == 0: return 0

            # if i, j in memo
            if (i, j) in memo: 
                return memo[(i, j)]

            # build up the answer at the current state
            
            if text1[i-1] == text2[j-1]: 
                ans = 1 + dp(i-1, j-1)
            else: 
                ans =  max(dp(i-1, j), dp(i, j-1))

            # store it in memo
            memo[(i, j)] = ans
            return ans
        
        return dp(len(text1), len(text2))



# dp[i][j] = length of the longest common subsequence found using the subset text1[1..i] and text2[1...j]

# base cases:
# dp[0][j] = 0 since text1 is empty
# dp[i][0] = 0 since text2 is empty
# dp[0][0] = 0 since both strings are empty

# recurrence: 
# At text1[i] and text2[j] you have the choices:
# 1) include text1[i] and text2[j] in the subsequence since they match
#     dp[i][j]
# 2) include the character that will give you the max length
#     dp[i-1][j] or dp[i][j-1]

# return dp[len(text1)][len(text2)]