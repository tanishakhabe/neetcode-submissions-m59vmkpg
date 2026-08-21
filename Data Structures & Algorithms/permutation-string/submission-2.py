class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False



        from collections import Counter
        s1_freq_map = Counter(s1)

        l = 0
        r = len(s1) - 1

        while l <= r and r < len(s2):
            s2_sub = s2[l:r+1]
            s2_freq_map = Counter(s2_sub)
            print(s2_freq_map)
            if s1_freq_map == s2_freq_map: 
                return True
            else:
                # adjust s2_window and s2_freq_map
                l += 1
                r += 1
        return False


            

        

        