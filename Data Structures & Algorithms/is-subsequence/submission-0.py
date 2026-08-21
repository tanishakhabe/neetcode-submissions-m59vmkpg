class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # is s in t? 

        curr_s = 0
        curr_t = 0

        # while both pointers are still valid, compare the current chars
        while curr_s < len(s) and curr_t < len(t):
            if t[curr_t] == s[curr_s]:
                curr_s += 1
            curr_t += 1

        # if reached end of T and chars still in S: 
        if curr_s < len(s): 
            return False

        # if reached end of S and chars still in T: 
        return True


        



        