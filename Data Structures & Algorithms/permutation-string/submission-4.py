class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        from collections import Counter
        s1_freq_map = Counter(s1)

        l = 0
        r = len(s1) - 1

        s2_sub = s2[l:r+1]
        s2_freq_map = Counter(s2_sub)

        while l <= r and r < len(s2):
            if s1_freq_map == s2_freq_map: 
                return True
            else:
                # adjust s2_window and s2_freq_map
                s2_freq_map[s2[l]] -= 1
                if s2_freq_map[s2[l]] == 0: s2_freq_map.pop(s2[l])
                l += 1

                if r < len(s2) - 1:
                    r += 1
                    if s2[r] in s2_freq_map:
                        s2_freq_map[s2[r]] += 1
                    else:
                        s2_freq_map[s2[r]] = 1

        return False


            

        

        