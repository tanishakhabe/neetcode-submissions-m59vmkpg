class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0

        count = {} # frequency of each character in the window

        for r in range(len(s)):
        
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l + 1) - max(count.values()) > k:
                # decrement count of old l
                # move left
                count[s[l]] -= 1
                l += 1

            # update res at end
            res = max(res, (r-l + 1))
        return res


            
             
        