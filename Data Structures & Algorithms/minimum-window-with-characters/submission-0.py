from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = None
        t_map = Counter(t)
        s_map = {}

        for r in range(0, len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)

            # while window valid: 
            while all(s_map.get(char, 0) >= t_map[char] for char in t_map):
                print("valid")
                
                # update ans
                window = s[l:r + 1]
                if ans is None or len(window) <= len(ans):
                    ans = window

                # try to shrink the curr window by remove arr[left] from curr map
                s_map[s[l]] -= 1
                l += 1

        if ans is None:
            return ""
        else: return ans

            
            
            
        